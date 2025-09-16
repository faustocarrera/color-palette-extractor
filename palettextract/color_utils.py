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
        '#ffffff',
        '#000000',
        '#333333',
        '#666666',
        '#999999',
        '#cccccc',
        '#cccc99',
        '#9999cc',
        '#666699',
        '#660000',
        '#663300',
        '#996633',
        '#003300',
        '#003333',
        '#003399',
        '#000066',
        '#330066',
        '#660066',
        '#990000',
        '#993300',
        '#cc9900',
        '#006600',
        '#336666',
        '#0033ff',
        '#000099',
        '#cc0000',
        '#cc3300',
        '#ffcc00',
        '#009900',
        '#006666',
        '#0066ff',
        '#0000cc',
        '#660099',
        '#663399',
        '#cc0099',
        '#990066',
        '#ff0000',
        '#ff3300',
        '#ffff00',
        '#00cc00',
        '#009999',
        '#0099ff',
        '#0000ff',
        '#9900cc',
        '#ff0099',
        '#cc3333',
        '#ff6600',
        '#ffff33',
        '#00ff00',
        '#00cccc',
        '#00ccff',
        '#3366ff',
        '#9933ff',
        '#ff00ff',
        '#ff6666',
        '#ff6633',
        '#ffff66',
        '#66ff66',
        '#66cccc',
        '#00ffff',
        '#ff9999',
        '#ff9966',
        '#ffff99',
        '#99ff99',
        '#66ffcc',
        '#99ffff',
        '#66ccff',
        '#9999ff',
        '#3399ff',
        '#9966ff',
        '#ff66ff',
        '#ff99ff',
        '#ffcccc',
        '#ffcc99',
        '#ffffcc',
        '#ccffcc',
        '#99ffcc',
        '#ccffff',
        '#99ccff',
        '#ccccff',
        '#ffccff',
    ]
