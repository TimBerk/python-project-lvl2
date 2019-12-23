# -*- coding:utf-8 -*-


def render_plain(data, parent=None):
    if parent is not None:
        name = parent.get('key')
        report = ['  ' + name + ': {']
    else:
        report = ['{']

    correct = [get_node(item, parent) for item in data.values()]

    report.append('\n'.join(correct))
    report.append('}')

    return '\n'.join(report)


def get_node(item, parent=None):
    type_item = item.get('type')
    name = item.get('key')
    result = ''

    if type_item == 'parent':
        result = render_plain(item.get('child'), item)
    elif type_item == 'changed':
        val = str(item.get('val'))
        old_val = str(item.get('old_val'))
        result += f"  - {name}: {val}\n"
        result += f"  + {name}: {old_val}"
    elif type_item == 'added':
        val = str(item.get('val'))
        result = f"  + {name}: {val}"
    elif type_item == 'deleted':
        val = str(item.get('val'))
        result = f"  - {name}: {val}"
    elif type_item == 'unchanged':
        val = str(item.get('val'))
        result = f"    {name}: {val}"

    return result
