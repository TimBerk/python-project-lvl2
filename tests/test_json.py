# -*- coding: utf-8 -*-

"""Tests for plain format"""

from gendiff.generator import generate_diff
from expected import JSON_STRING, COMPLEX_JSON


def test_correct_function():
    expected = JSON_STRING
    actual = generate_diff('./tests/fixtures/plain_before.json',
                           './tests/fixtures/plain_after.json',
                           'json')
    assert actual == expected


def test_usupported_formatter():
    expected = 'Incorrect format'
    actual = generate_diff('./tests/fixtures/plain_before.json',
                           './tests/fixtures/plain_after.json',
                           'deadbeef')
    assert actual == expected


def test_correct_complex_function():
    expected = COMPLEX_JSON
    actual = generate_diff('./tests/fixtures/complex_diff_before.json',
                           './tests/fixtures/complex_diff_after.json',
                           'json')
    assert actual == expected
