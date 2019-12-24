# -*- coding:utf-8 -*-


def render_yml(data, parent=None, deep=0):
    if parent is not None:
        name = parent.get('app_key')
        report = [deep * '  ' + name + ':']
    else:
        report = []

    correct = [get_node(item, parent, deep) for item in data.values()]
    report.append('\n'.join(correct))

    return '\n'.join(report)


def get_node(item, parent=None, deep=0):
    type_item = item.get('type')
    name = item.get('app_key')
    result = ''
    start = deep * "  "
    start_in = (deep + 1) * "  "

    if type_item == 'parent':
        result = render_yml(item.get('child'), item, deep=deep+1)
    elif type_item == 'changed':
        val = get_value(item.get('val'))
        old_val = get_value(item.get('old_val'), deep)
        result += start + f"{name}:\n"
        result += start_in + f"+ val: {val}\n"
        result += start_in + f"- old_val: {old_val}"
    elif type_item == 'added':
        val = get_value(item.get('val'), deep)
        result = start + f"{name}:\n"
        result += start_in + f"+ val: {val}"
    elif type_item == 'deleted':
        val = get_value(item.get('val'), deep)
        result = start + f"{name}:\n"
        result += start_in + f"- val: {val}"
    elif type_item == 'unchanged':
        val = get_value(item.get('val'), deep)
        result = start + f"{name}:\n"
        result += start_in + f"  val: {val}"

    return result


def get_value(value, deep=0):
    if isinstance(value, dict):
        start = (deep * "    ")[0:-2]
        for key, val in value.items():
            name, value = key, val
        value += start + f"\n"
        value += start + f"    {name}: {val}\n"

    return str(value)
