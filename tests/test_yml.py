# -*- coding: utf-8 -*-

"""Tests for yaml format"""

from gendiff.generator import generate_diff
from expected import SIMPLE_STRING, YAML_STRING
from expected import COMPLEX_YAML, COMPLEX_JSON


def test_plain_format():
    expected = SIMPLE_STRING
    actual = generate_diff('./tests/fixtures/yaml_before.yml',
                           './tests/fixtures/yaml_after.yml',
                           'string')
    assert actual == expected


def test_yaml_format():
    expected = YAML_STRING
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
    expected = COMPLEX_YAML
    actual = generate_diff('./tests/fixtures/complex_diff_before.yml',
                           './tests/fixtures/complex_diff_after.yml',
                           'yml')
    assert actual == expected


def test_correct_json_function():
    expected = COMPLEX_JSON
    actual = generate_diff('./tests/fixtures/complex_diff_before.yml',
                           './tests/fixtures/complex_diff_after.yml',
                           'json')
    assert actual == expected
