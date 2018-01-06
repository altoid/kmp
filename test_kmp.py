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

    def test_match(self):
        pattern = 'abcdabd'
        text = 'abc abcdab abcdabcdabde'
        result = kmp.match(pattern, text)
        self.assertEqual([15], result)

    def test_pattern_is_text(self):
        pattern = 'abcdabd'
        result = kmp.match(pattern, pattern)
        self.assertEqual([0], result)

    def test_no_match(self):
        pattern = 'zzyzyvq'
        text = 'abc abcdab abcdabcdabde'
        result = kmp.match(pattern, text)
        self.assertEqual([], result)

    def test_gattaca(self):
        sequence = (
            'GACTTTTTTTTTTTTTCCTTTGGGAAAGGTAGGGAGGTGTTCGTACGGGAGCAGCCTCGG'
            'GGACCCCTGCACTGGGTCAGGGCTTATGAAGCTAGAAGCGTCCCTCTGTTCCCTTTGTGA'
            'GTTGGTGGGTTGTTGGTACATTTGGTTGGAAGCTGTGTTGCTGGTTAGGGAGACTCGGTT'
            'TTGCTCCTTGGGTTCGAGGAAAGCTGGAGAATAGAAGCCATTGTTTGCCGTCTGTCGGCT'
            'TTGTCGACCACGCTCACCCCCTCCTGTTCGTACTTTTTAAAGCAGTGAGGCGAGGTAGAC'
            'AGGGTGTGTCACAGTACAGTTAAAGGGGTGAAGATCTAAACGCCAAAAGAGAAGTTAATC'
            'ACAATAAGTGAGGTTTGGGATAAAAAGTTGGGCTTGCCCCTTTCAAAGTCCCAGAAAGCT'
            'GGGAGGTAGATGGAGAGGGGGCCATTGGGAAGTTTTTTTGGTGTAGGGAGAGGAGTAGAA'
            'GATAAAGGGTAAGCAGAGTGTTGGGTTCTGGGGGTCTTGTGAAGTTCCTTAAGGAAGGAG'
            'GGAGTGTGGCCCTGCAGCCCTCCCAAACTGCTCCAGCCTATGCTCTCCGGCACCAGGAAG'
            'TTCCAAGGTTCCCTTCCCCTGGTCTCCAAACTTCAGGTATTCCTCTCCCCTCACACCCCT'
            'TCAACCTCAGCTCTTGGCCTCTACTCCTTACTCCACTGTTCCTCCTGTTTCCCCCTTCCC'
            'CTTTTCCTGGTTCTTTATATTTTTGCAAAGTGGGATCCGAACTTGCTAGATTTTCCAATT'
            'CTCCCAAGCCAGACCAGAGCAGCCTCTTTTAAAGGATGGAGACTTCTGTGGCAGATGCCG'
            'CTGAAAATGTGGGTGTAATGCTGGGACTTAGAGTTTGATGACAGTTTGACTGAGCCCTAG'
            'ATGCATGTGTTTTTCCTGAGAGTGAGGCTCAGAGAGCCCATGGACGTATGCTGTTGAACC'
            'ACAGCTTGATATACCTTTTTCTCCTTCTGTTTTGTCTTAGGGGGAAGACTTTAACTAGGG'
            'GCGCGCAGATGTGTGAGGCCTTTTATTGTGAGAGTGGACAGACATCCGAGATTTCAGGCA'
            'AGTTCTGTGGTGGCTGCTTTGGGCT'
        )

        print len(sequence)
        print kmp.match('CAT', sequence)
        print kmp.match('GGCAA', sequence)