#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Color extractor
Extract the most dominant colors from an image using Click for command-line interface.
Supports both individual files and batch processing of folders.
"""

from pathlib import Path
import click
from palettextract import ColorExtractor

@click.command()
@click.argument('input_path', type=click.Path(exists=True, path_type=Path))
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
def extract(input_path: Path, verbose: bool):
    """
    Extract the most dominant colors from an image.
    INPUT_PATH can be either a single image file or a directory containing images.
    """
    extractor = ColorExtractor(verbose=verbose)
    color_palette = extractor.color_palette(input_path)
    print(color_palette)

if __name__ == "__main__":
    extract()
