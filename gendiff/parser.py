# -*- coding:utf-8 -*-
import json
import yaml


def parser(file, extension):
    """Parser data into nececcary format"""
    parse_map = {
        '.json': json.loads,
        '.yml': yaml.safe_load
    }

    return parse_map[extension](file)
