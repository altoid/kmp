#!/usr/bin/env python

import unittest
import kmp
import pprint

pp = pprint.PrettyPrinter(width=50)


class TestKMP(unittest.TestCase):

    def test_overlap(self):
        pattern = 'abababcab'
        f = kmp.overlap(pattern)
        self.assertTrue(len(pattern) == len(f))
        self.assertEqual([0, 0, 1, 2, 3, 4, 0, 1, 2], f)

    def test_singleton_pattern(self):
        pattern = 'a'
        f = kmp.overlap(pattern)
        self.assertTrue(len(pattern) == len(f))
        self.assertEqual(0, f[0])
