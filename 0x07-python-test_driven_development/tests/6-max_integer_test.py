#!/usr/bin/python3
"""
Tests '6-max_integer' module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define tests methods, each to start with 'test'"""

    def test_values(self):
        """Returns None for an empty list.."""
        self.assertEqual(max_integer(list=[5, 4, 6]), 6, "should be 6")
        self.assertEqual(max_integer(list=[100, 5000, 2]), 5000)
        self.assertEqual(max_integer(list=[]), None)
        self.assertEqual(max_integer(list=[6]), 6)
        self.assertEqual(max_integer(list=[-1, -6, -8]), -1)

    def test_exceptions(self):
        """Check for exceptions raised"""
        self.assertRaises(TypeError, max_integer, ['str', 5, 8, 4])
        self.assertRaises(TypeError, max_integer, {10, 5, 6, 17})
