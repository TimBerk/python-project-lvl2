# -*- coding: utf-8 -*-

"""Expected results"""

PLAIN_STRING = """{
    host: hexlet.io
  - proxy: 123.234.53.22
  + timeout: 20
  - timeout: 50
  + verbose: true
}"""

YAML_STRING = """host:
  - val: hexlet.io
proxy:
  - val: 123.234.53.22
timeout:
  - val: 20
  - old_val: 50
verbose:
  - val: true
"""
