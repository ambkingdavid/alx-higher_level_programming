#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer



class TestMaxInteger(unittest.TestCase):
    """ it defines a tester for max_integer"""

    def test_check_max(self):
        """test for the max number in a ordered list"""
        mylist = [1, 2, 3, 4]
        max_val = max_integer([1,2,3,4])
        self.assertEqual(max_val, 4)

    def test_check_max_empty(self):
        """test for max in an empty list"""
        mylist = []
        self.assertEqual(max_integer(mylist), None)

    def test_check_max_unordered(self):
        """tests for max in an unordered list"""
        mylist = [2, 4, 1, 3]
        self.assertEqual(max_integer(mylist), 4)

    def test_check_max_negative(self):
        """tests for max in a list of negative numbers"""
        mylist = [-1, -4, -2, -3]
        self.assertEqual(max_integer(mylist), -1)



#if __name__ == '__main__':
 #   unittest.main()
