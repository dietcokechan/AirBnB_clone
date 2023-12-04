#!/usr/bin/python3
"""tests for console"""
import unittest
import pep8


class TestConsole(unittest.TestCase):
    """tests console"""

    def test_pep8_console(self):
        """Pep8 test"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')