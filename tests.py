import unittest

import seq_utils


class TestSeqUtils(unittest.TestCase):
	def test_is_codon_correct(self):
		codon = 'ATG'
		result = seq_utils.is_codon_correct(codon)
		expected = True
		self.assertEqual(expected, result)
		
	def test_is_codon_correct_bad_codon1(self):
		codon = 'A2G'
		result = seq_utils.is_codon_correct(codon)
		expected = False
		self.assertEqual(expected, result)
		
	def test_is_codon_correct_bad_codon2(self):
		codon = 3.1416
		result = seq_utils.is_codon_correct(codon)
		expected = False
		self.assertEqual(expected, result)
	
