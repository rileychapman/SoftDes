# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 10:40:40 2014

@author: pruvolo
"""

import unittest

def in_language(s):
	numAs = s.count('a')
	numBs = s.count('b')
	if numAs + numBs != len(s):
		return False
	if numBs != numAs:
		return False

	if s[0:len(s)/2] != 'a'*(len(s)/2):
		return False

	return True

class InLanguageTests(unittest.TestCase):
    def test_in_language_basic(self):
        self.assertFalse(in_language('aaab'))
        self.assertFalse(in_language('aaaccc'))
        self.assertTrue(in_language(''))
        self.assertTrue(in_language('aaaabbbb'))
        self.assertFalse(in_language('abab'))
        self.assertFalse(in_language('aaacbbb'))

if __name__ == '__main__':
    unittest.main()