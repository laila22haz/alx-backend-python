#!/usr/bin/env python3
"""Test cases for our lovely acssec_nested_map function
"""
from parameterized import parameterized
from typing import Dict
import unittest
import requests
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """test the getJson function"""
    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests) -> Dict:
        """test the getJeson function"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests.return_value = mock_response
        result = get_json(test_url)
        mock_requests.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """test memoize function"""
    def test_memoize(self):
        """test memoize function"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42
                          ) as mock_memoize:

            mock_response = TestClass()
            response1 = mock_response.a_property
            response2 = mock_response.a_property
            mock_memoize.assert_called_once()
            self.assertEqual(response1, 42)
            self.assertEqual(response2, 42)


if __name__ == "__main__":
    unittest.main()
