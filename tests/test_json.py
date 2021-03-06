# -*- coding: utf-8 -*-

"""Tests for plain format"""

from gendiff.generator import generate_diff
from read_correct_file import read_data


def test_correct_function():
    expected = read_data('simple.json', format='json')
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
    expected = read_data('complex.json', format='json')
    actual = generate_diff('./tests/fixtures/complex_diff_before.json',
                           './tests/fixtures/complex_diff_after.json',
                           'json')
    assert actual == expected
