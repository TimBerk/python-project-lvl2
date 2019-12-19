# -*- coding:utf-8 -*-


def render_plain(data):
    """Parser data into plain format"""
    report = ['{']

    for key in data:
        correct = ''
        item = data[key]

        if 'old_val' in item:
            correct = f"  {item['type']} {item['key']}: {str(item['val'])}\n"
            correct += f"  - {item['key']}: {str(item['old_val'])}"
        else:
            correct = f"  {item['type']} {item['key']}: {str(item['val'])}"
        report.append(correct)
    report.append('}')

    print('\n'.join(report))
    return report
