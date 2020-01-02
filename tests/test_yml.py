# -*- coding: utf-8 -*-

"""Tests for yaml format"""

from gendiff.generator import generate_diff
from read_correct_file import read_data


def test_plain_format():
    expected = read_data('simple.txt')
    actual = generate_diff('./tests/fixtures/yaml_before.yml',
                           './tests/fixtures/yaml_after.yml',
                           'string')
    assert actual == expected


def test_yaml_format():
    expected = read_data('simple.yml', format='yml')
    actual = generate_diff('./tests/fixtures/yaml_before.yml',
                           './tests/fixtures/yaml_after.yml',
                           'yml')
    assert actual == expected


def test_usupported_formatter():
    expected = 'Incorrect format'
    actual = generate_diff('./tests/fixtures/yaml_before.yml',
                           './tests/fixtures/yaml_after.yml',
                           'deadbeef')
    assert actual == expected


def test_correct_complex_function():
    expected = read_data('complex.yml', format='yml')
    actual = generate_diff('./tests/fixtures/complex_diff_before.yml',
                           './tests/fixtures/complex_diff_after.yml',
                           'yml')
    assert actual == expected


def test_correct_json_function():
    expected = read_data('complex.json', format='json')
    actual = generate_diff('./tests/fixtures/complex_diff_before.yml',
                           './tests/fixtures/complex_diff_after.yml',
                           'json')
    assert actual == expected
