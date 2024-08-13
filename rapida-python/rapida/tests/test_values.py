"""
author: prashant.srivastav
"""
import unittest
from google.protobuf.any_pb2 import Any
from google.protobuf.wrappers_pb2 import StringValue

from rapida.values import String


class TestStringFunction(unittest.TestCase):
    def setUp(self):
        """Set up any necessary test data or state."""
        self.test_string = "Hello, world!"

    def test_string_packing(self):
        """Test that the `String` function correctly packs a string into Any."""
        any_message = String(self.test_string)

        # Assert that any_message is of type Any
        self.assertIsInstance(any_message, Any)

        # Unpack the Any object
        unpacked_string_value = StringValue()
        self.assertTrue(any_message.Unpack(unpacked_string_value))

        # Assert that the unpacked string matches the original string
        self.assertEqual(unpacked_string_value.value, self.test_string)

    def test_string_empty(self):
        """Test the `String` function with an empty string."""
        any_message = String("")

        # Assert that any_message is of type Any
        self.assertIsInstance(any_message, Any)

        # Unpack the Any object
        unpacked_string_value = StringValue()
        self.assertTrue(any_message.Unpack(unpacked_string_value))

        # Assert that the unpacked string is empty
        self.assertEqual(unpacked_string_value.value, "")

    def test_string_invalid_type(self):
        """Test the `String` function with an invalid type (should handle errors)."""
        with self.assertRaises(TypeError):
            # Intentionally passing an integer to see if it raises an error
            String(123)  # This should raise an error if type checking is enforced

