# -*- coding: utf-8 -*-

"""Tests for yaml format"""

from gendiff.generator import generate_diff
from expected import PLAIN_STRING, YAML_STRING


def test_plain_format():
    expected = PLAIN_STRING
    actual = generate_diff('./tests/fixtures/yaml_before.yml',
                           './tests/fixtures/yaml_after.yml',
                           'plain')
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
