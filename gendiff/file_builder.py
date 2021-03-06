# -*- coding:utf-8 -*-


def builder_report(first, second):
    """Find difference and return list of them"""

    main_list = list(first.keys() | second.keys())
    result = {key: find_diff(key, first, second) for key in sorted(main_list)}
    return result


def find_diff(key, first, second):
    """Find difference between two value by key"""

    diff = {}
    first_val = first.get(key)
    second_val = second.get(key)

    if first_val is None:
        diff = {
            'type': 'added',
            'app_key': key,
            'val': get_right_value(second_val)
        }
    elif second_val is None:
        diff = {
            'type': 'deleted',
            'app_key': key,
            'val': get_right_value(first_val)
        }
    elif isinstance(first_val, dict) and isinstance(second_val, dict):
        result = builder_report(first_val, second_val)
        diff = {
            'type': 'parent',
            'app_key': key,
            'child': result
        }
    elif first_val == second_val:
        diff = {
            'type': 'unchanged',
            'app_key': key,
            'val': get_right_value(second_val)
        }
    elif first_val != second_val:
        diff = {
            'type': 'changed',
            'app_key': key,
            'val': get_right_value(second_val),
            'old_val': get_right_value(first_val)
        }

    return diff


def get_right_value(var):
    """Find correct value of variable"""

    if var is True:
        return 'true'
    if var is False:
        return 'false'

    return var
