#!/usr/bin/python3
""" """
from console import HBNBCommand
import unittest
import sys
from io import StringIO

class test_console(unittest.TestCase):
    """
    testing the console
    """

    def test_create(self):
        """tests the create module"""
        old_stdout = sys.stdout
        sys.stdout = testId = StringIO()
        HBNBCommand().do_create("User first_name=\"seb\"")
        sys.stdout = User = StringIO()
        HBNBCommand().do_show("User " +testId.getvalue()[:-1])
        sys.stdout = old_stdout
        self.assertEqual(User.getvalue()[-21:-2],"'first_name': 'seb'")


