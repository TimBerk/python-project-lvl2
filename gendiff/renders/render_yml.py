# -*- coding:utf-8 -*-


def render_yml(data):
    """Parser data into yml format"""
    report = ''

    for key in data:
        correct = ''
        item = data[key]

        if 'old_val' in item:
            correct += f"{item['key']}:\n" \
                    + f"  - val: {str(item['val'])}\n" \
                    + f"  - old_val: {str(item['old_val'])}\n"
        else:
            correct += f"{item['key']}:\n"
            correct += f"  - val: {str(item['val'])}\n"
        report += correct

    return report
