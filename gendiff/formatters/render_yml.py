# -*- coding:utf-8 -*-


def render_yml(data, parent=None, deep=0):
    report = []

    correct = [get_node(item, parent, deep) for item in data.values()]
    report.append('\n'.join(correct))

    return '\n'.join(report)


def get_node(item, parent=None, deep=0):
    start = deep * "  "
    start_in = start + "  "

    type_item = item.get('type')
    name = item.get('app_key')

    result = start + f'{name}' + ':\n'
    result += start_in + f'type: {type_item}\n'
    result += start_in + f'key: {name}\n'

    if type_item == 'parent':
        child = render_yml(item.get('child'), item, deep=deep+2)
        result += start_in + f'child:\n' + child
    elif type_item == 'changed':
        val = get_value(item.get('val'), deep)
        old_val = get_value(item.get('old_val'), deep)
        result += start_in + f"{val}\n"
        result += start_in + f"old_{old_val}"
    elif type_item == 'added':
        val = get_value(item.get('val'), deep)
        result += start_in + f"{val}"
    elif type_item == 'deleted':
        val = get_value(item.get('val'), deep)
        result += start_in + f"{val}"
    elif type_item == 'unchanged':
        val = get_value(item.get('val'), deep)
        result += start_in + f"{val}"

    return result


def get_value(value, deep=0):
    if isinstance(value, dict):
        if deep == 2:
            start = (deep + 3) * "  "
            start = start[0:-2]
        else:
            start = (deep + 2) * "  "

        for key, val in value.items():
            name, value = key, val
        value = 'val:\n'
        value += start + f'{name}: {val}'
    else:
        value = f"val: {value}"

    return value
