# -*- coding: utf-8 -*-

"""Tests for plain format"""

from gendiff.generator import generate_diff
from expected import SIMPLE_STRING, COMPLEX_STRING, PLAIN_STRING


def test_correct_function():
    expected = SIMPLE_STRING
    actual = generate_diff('./tests/fixtures/plain_before.json',
                           './tests/fixtures/plain_after.json',
                           'string')
    assert actual == expected


def test_usupported_formatter():
    expected = 'Incorrect format'
    actual = generate_diff('./tests/fixtures/plain_before.json',
                           './tests/fixtures/plain_after.json',
                           'deadbeef')
    assert actual == expected


def test_correct_diff_function():
    expected = COMPLEX_STRING
    actual = generate_diff('./tests/fixtures/plain_diff_before.json',
                           './tests/fixtures/plain_diff_after.json',
                           'string')
    assert actual == expected


def test_correct_plain_function():
    expected = PLAIN_STRING
    actual = generate_diff('./tests/fixtures/plain_diff_before.json',
                           './tests/fixtures/plain_diff_after.json',
                           'plain')
    assert actual == expected
