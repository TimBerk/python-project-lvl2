# -*- coding:utf-8 -*-


def render_json(data, parent=None, deep=1):
    report = ['{']

    if deep == 2:
        start_in = (deep) * "    "
    else:
        start_in = (deep - 1) * "    "

    correct = [get_node(item, parent, deep) for item in data.values()]

    report.append(',\n'.join(correct))
    end = start_in + '}'
    report.append(end)

    return '\n'.join(report)


def get_node(item, parent=None, deep=0):

    if deep > 1:
        start_in = (deep + 1) * "    "
    else:
        start_in = deep * "    "

    start = start_in + "    "

    type_item = item.get('type')
    name = item.get('app_key')

    result = start_in + f'"{name}"' + ': {\n'
    result += start + f'"type": "{type_item}",\n'
    result += start + f'"key": "{name}",\n'

    if type_item == 'parent':
        child = render_json(item.get('child'), item, deep=deep+1)
        result += start + f'"child": ' + child + '\n'
    elif type_item == 'changed':
        val = get_value(item.get('val'))
        old_val = get_value(item.get('old_val'), deep)
        result += start + f'"val": {val},\n'
        result += start + f'"old_val": {old_val}\n'
    elif type_item == 'added':
        val = get_value(item.get('val'), deep)
        result += start + f'"val": {val}\n'
    elif type_item == 'deleted':
        val = get_value(item.get('val'), deep)
        result += start + f'"val": {val}\n'
    elif type_item == 'unchanged':
        val = get_value(item.get('val'), deep)
        result += start + f'"val": {val}\n'

    result += start_in + '}'
    return result


def get_value(value, deep=2):
    if isinstance(value, dict):
        if deep == 2:
            start = (deep + 3) * "    "
        else:
            start = (deep + 2) * "    "
        start_in = start[0:-4]

        for key, val in value.items():
            name, value = key, val
        value = "{\n"
        value += start + f'"{name}": "{val}"\n'
        value += start_in + "}"
    else:
        value = '"' + str(value) + '"'
    return value
