# -*- coding:utf-8 -*-
from gendiff.renders.render_plain import render_plain
from gendiff.renders.render_yml import render_yml


def render(file, extension):
    """Render data into necessary format"""
    parse_map = {
        'plain': render_plain,
        'yml': render_yml
    }

    if extension not in parse_map:
        return "Incorrect format"

    return parse_map[extension](file)
