#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utils
"""

from os import path
from datetime import datetime


class VerboseLogger:
    "Verbose logger"

    def __init__(self, verbose: bool):
        self.verbose = verbose

    def log(self, message: str):
        "Print message just if the verbose flag is set"
        if self.verbose:
            print(f"{message}")


def get_destination_path(folder, name):
    "Get destination path"
    return path.join(folder, name) if folder else name


def get_file_dir(file_path):
    "Get directory based on path"
    return path.dirname(path.realpath(file_path))


def get_filename(name, new_name):
    "change names but keep the ext"
    parts = name.split('.')
    return f"{new_name}.{parts[-1]}"


def get_name_by_path(file_path, sufix=True):
    "Get name based on path"
    if sufix:
        return file_path.name
    return file_path.stem


def sort_by_count(tuple_to_sort):
    "Sort tuple by value"
    sorted_tuple = sorted(tuple_to_sort, key=lambda x: x[0], reverse=True)
    return sorted_tuple


def get_current_date():
    "Get current date and time in ISO format"
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
