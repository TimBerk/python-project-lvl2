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
    val: hexlet.io
proxy:
  - val: 123.234.53.22
timeout:
  + val: 20
  - old_val: 50
verbose:
  + val: true"""

JSON_STRING = """{
    "host": {
        "type": "unchanged",
        "key": "host",
        "val": "hexlet.io"
    },
    "proxy": {
        "type": "deleted",
        "key": "proxy",
        "val": "123.234.53.22"
    },
    "timeout": {
        "type": "changed",
        "key": "timeout",
        "val": "20",
        "old_val": "50"
    },
    "verbose": {
        "type": "added",
        "key": "verbose",
        "val": "true"
    }
}"""

COMPLEX_STRING = """{
    common: {
      setting1: Value 1
    - setting2: 200
      setting3: true
    + setting4: blah blah
    + setting5: {
          key5: value5
      }
    - setting6: {
          key: value
      }
  }
    group1: {
    + baz: bars
    - baz: bas
      foo: bar
  }
  - group2: {
        abc: 12345
    }
  + group3: {
        fee: 100500
    }
}"""

COMPLEX_JSON = '''{
    "common": {
        "type": "parent",
        "key": "common",
        "child": {
            "setting1": {
                "type": "unchanged",
                "key": "setting1",
                "val": "Value 1"
            },
            "setting2": {
                "type": "deleted",
                "key": "setting2",
                "val": "200"
            },
            "setting3": {
                "type": "unchanged",
                "key": "setting3",
                "val": "true"
            },
            "setting4": {
                "type": "added",
                "key": "setting4",
                "val": "blah blah"
            },
            "setting5": {
                "type": "added",
                "key": "setting5",
                "val": {
                    "key5": "value5"
                }
            },
            "setting6": {
                "type": "deleted",
                "key": "setting6",
                "val": {
                    "key": "value"
                }
            }
        }
    },
    "group1": {
        "type": "parent",
        "key": "group1",
        "child": {
            "baz": {
                "type": "changed",
                "key": "baz",
                "val": "bars",
                "old_val": "bas"
            },
            "foo": {
                "type": "unchanged",
                "key": "foo",
                "val": "bar"
            }
        }
    },
    "group2": {
        "type": "deleted",
        "key": "group2",
        "val": {
            "abc": "12345"
        }
    },
    "group3": {
        "type": "added",
        "key": "group3",
        "val": {
            "fee": "100500"
        }
    }
}'''
