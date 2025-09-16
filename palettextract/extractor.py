#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Color Extractor
Extract the most dominant colors from an image and create a color palette.
"""

from pathlib import Path
import pandas as pd
from PIL import Image
from PIL import ImageDraw
from . import color_utils as cu
from . import utils as pu


class ColorExtractor():
    """
    Color extractor
    Extract the most dominant colors from an image and create a color palette.
    """

    def __init__(self, verbose=False):
        self.limit = 64
        self.size = 1020
        self.logger = pu.VerboseLogger(verbose)

    def color_palette(self, input_path: Path) -> str:
        "Generate the color palette"
        self.logger.log(f"Extracting colors from {input_path}")
        image = Image.open(input_path).convert('RGB')
        colors = self.__get_colors(image)
        palette = self.__generate_palette(
            colors,
            pu.get_file_dir(input_path),
            pu.get_name_by_path(input_path, False)
        )
        return palette

    def __get_colors(self, image):
        "Get colors in image"
        colors = []
        colors_tmp = {}
        parents = []
        # resize the image to speed up the processing
        thumb = image.resize((300, 300), resample=Image.NEAREST)
        image_colors = thumb.getcolors(1600*1600)
        # arrange the colors
        for color in image_colors:
            parent = self.__get_parent(color)
            if parent not in colors_tmp:
                colors_tmp[parent] = []
                parents.append(parent)
            colors_tmp[parent].append((color[0], cu.rgb_to_hex(color[1])))
        # filter them
        for color in parents:
            color_series = pd.Series(pu.sort_by_count(colors_tmp[color]))
            colors_sample = color_series.sample(n=25, replace=True)
            for color_sample in colors_sample:
                colors.append({'parent': color, 'color': color_sample})
        # return just a sample
        palette_series = pd.Series(colors)
        return palette_series.sample(n=self.limit, replace=False)

    def __get_parent(self, color):
        "Return closer color"
        color_distance = None
        color_parent = None
        base_colors = cu.get_base_colors()
        for base in base_colors:
            base_rgb = cu.hex_to_rgb(base)
            distance = cu.get_color_distance(base_rgb, color[1])
            if color_distance is None or distance < color_distance:
                color_distance = distance
                color_parent = base
        return color_parent

    def __generate_palette(self, colors, folder, name) -> str:
        "Generate paletter from image"
        filename = pu.get_destination_path(folder, f"palette_{name}.png")
        x_pos, y_pos = 10, 10
        sqr_side = 125
        count = 0
        image = Image.new('RGB', (self.size, self.size), '#fbfbfb')
        draw = ImageDraw.Draw(image)
        for color in colors:
            position = [x_pos, y_pos, (x_pos + sqr_side), (y_pos + sqr_side)]
            draw.rectangle(
                position,
                fill=color['color'][1],
                outline=None,
                width=0
            )
            y_pos += sqr_side
            if count >= 7:
                count = 0
                x_pos += sqr_side
                y_pos = 10
            else:
                count += 1

        image.save(filename, format='PNG', quality=95)
        return filename
