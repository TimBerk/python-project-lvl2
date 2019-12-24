# -*- coding:utf-8 -*-


def render_plain(data, parent=None, deep=1):
    if parent is not None:
        name = parent.get('app_key')
        report = [deep * '  ' + name + ': {']
    else:
        report = ['{']

    correct = [get_node(item, parent, deep) for item in data.values()]

    report.append('\n'.join(correct))
    end = deep * ' ' + '}' if parent is not None else '}'
    report.append(end)

    return '\n'.join(report)


def get_node(item, parent=None, deep=0):
    type_item = item.get('type')
    name = item.get('app_key')
    result = ''
    start = deep * "  "

    if type_item == 'parent':
        result = render_plain(item.get('child'), item, deep=deep+1)
    elif type_item == 'changed':
        val = get_value(item.get('val'))
        old_val = get_value(item.get('old_val'), deep)
        result += start + f"+ {name}: {val}\n"
        result += start + f"- {name}: {old_val}"
    elif type_item == 'added':
        val = get_value(item.get('val'), deep)
        result = start + f"+ {name}: {val}"
    elif type_item == 'deleted':
        val = get_value(item.get('val'), deep)
        result = start + f"- {name}: {val}"
    elif type_item == 'unchanged':
        val = get_value(item.get('val'), deep)
        result = start + f"  {name}: {val}"

    return result


def get_value(value, deep=0):
    if isinstance(value, dict):
        if deep == 1:
            start = deep * "    "
        else:
            start = (deep * "    ")[0:-2]
        for key, val in value.items():
            name, value = key, val
        value = "{\n"
        value += start + f"    {name}: {val}\n"
        value += start + "}"

    return str(value)
