# -*- coding:utf-8 -*-
import os

from gendiff.parser import parser
from gendiff.file_builder import builder_report
from gendiff.renders.render import render


def read_file(file_input):

    with open(file_input, 'r', encoding='utf-8') as file:
        file_extension = os.path.splitext(file_input)[1]
        content = file.read()
        return parser(content, file_extension)


def generate_diff(first_file, sencond_file, format_file=None):
    if format_file is None:
        format_file = 'plain'

    first, second = read_file(first_file), read_file(sencond_file)
    difference = builder_report(first, second)
    report = render(difference, format_file)
    return report
