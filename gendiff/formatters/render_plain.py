# -*- coding:utf-8 -*-


def render_plain(data, parent=None):
    report = []

    correct = [get_node(item, parent=parent) for item in data.values()]

    str_list = list(filter(None, correct))
    report.append('\n'.join(str_list))
    return '\n'.join(report)


def get_node(item, parent=None):
    type_item = item.get('type')
    name = item.get('app_key')

    if parent is not None:
        name_parent = parent.get('app_key')
        name = ".".join([name_parent, name])
    result = ''

    if type_item == 'parent':
        result = render_plain(item.get('child'), parent=item)
    elif type_item == 'changed':
        val = get_value(item.get('val'))
        old_val = get_value(item.get('old_val'))
        result = f"Property '{name}' was changed. From '{old_val}' to '{val}'"
    elif type_item == 'added':
        val = get_value(item.get('val'))
        result = f"Property '{name}' was added with value: '{val}'"
    elif type_item == 'deleted':
        val = get_value(item.get('val'))
        result = f"Property '{name}' was removed"
    elif type_item == 'uncahnged':
        result = None

    return result


def get_value(value):
    if isinstance(value, dict):
        for key, val in value.items():
            value = 'complex value'

    return str(value)
