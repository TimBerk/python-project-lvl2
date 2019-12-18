# -*- coding:utf-8 -*-
import json


def parser(file, extension):
    """Parser data into nececcary format"""
    parse_map = {
        '.json': json.loads
    }

    return parse_map[extension](file)
