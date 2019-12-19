# -*- coding:utf-8 -*-
from gendiff.renders.render_plain import render_plain


def render(file, extension):
    """Render data into necessary format"""
    parse_map = {
        'plain': render_plain
    }

    if extension not in parse_map:
        return "Incorrect format"

    return parse_map[extension](file)
