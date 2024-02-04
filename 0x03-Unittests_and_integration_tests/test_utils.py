#!/usr/bin/env python3
"""Test cases for our lovely acssec_nested_map function
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """let's start testing our nestedMap"""
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {'b': 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ])
    def test_access_nested_map(self, nested_map, path, expected) -> None:
        """test the access_nested_map function"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([({}, ("a",), KeyError), (
            {"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test access_nested_map with exception"""
        with self.assertRaises(KeyError) as context:
            context = access_nested_map(nested_map, path)
            self.assertRaises(context, expected)


if __name__ == "__main__":
    unittest.main()
