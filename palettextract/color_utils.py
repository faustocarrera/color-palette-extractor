#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Functions related with colors
"""

import math


def get_color_distance(acolor, bcolor):
    "Return the distance between two colors"
    distance = math.pow(
        (bcolor[0] - acolor[0]), 2
    ) + math.pow(
        (bcolor[1] - acolor[1]), 2
    ) + math.pow(
        (bcolor[2] - acolor[2]), 2
    )
    return math.sqrt(distance)


def hex_to_rgb(color):
    "Convert color from HEX to RGB"
    color = color.lstrip('#')
    return (int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16))


def rgb_to_hex(rgb):
    "Convert RGB to Hex"
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


def get_base_colors():
    "Base colors"
    return [
        '#000000',
        '#808080',
        '#c0c0c0',
        '#ffffff',
        '#800000',
        '#ff0000',
        '#008000',
        '#00ff00',
        '#808000',
        '#ffff00',
        '#008080',
        '#00ffff',
        '#000080',
        '#0000ff',
        '#800080',
        '#ff00ff'
    ]
