#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scans directories for image files.
Supports common image formats: jpg, jpeg, png, gif, bmp
"""

from pathlib import Path
from typing import List


class ImageScanner:
    "Scans directories for image files."

    def __init__(self):
        self.supported_formats = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    def scan_directory(self, input_path: Path) -> List[Path]:
        "Scans a directory or validates a single image and returns a list of paths to image files."

        # Check if path exists
        if not input_path.exists():
            raise ValueError(f"Invalid path: {input_path}")

        # Handle single image file
        if input_path.is_file():
            if input_path.suffix.lower() in self.supported_formats:
                return [input_path]
            raise ValueError(f"Unsupported file format: {input_path.suffix}")

        # Handle directory
        if input_path.is_dir():
            image_files = []
            for ext in self.supported_formats:
                image_files.extend(input_path.glob(f"*{ext}"))
                # Also check for uppercase extensions
                image_files.extend(input_path.glob(f"*{ext.upper()}"))
            # remove duplicates and sort
            image_files = list(set(image_files))
            return sorted(image_files)

        raise ValueError(
            f"Path is neither a file nor a directory: {input_path}")
