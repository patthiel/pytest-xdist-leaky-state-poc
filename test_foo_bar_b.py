import unittest
from test import test_dictionary

class FooBarCTest(unittest.TestCase):
	def test_well_shit(self):
		self.assertEqual(test_dictionary["foo"], "bar")
		# After the test, let's do something rude to our variable:
		test_dictionary["foo"] = "well, crap..."

class FooBarDTest(unittest.TestCase):
	def test_oh_boy(self):
		self.assertEqual(test_dictionary["foo"], "bar")
		# After this one let's do that too:
		# This should fail because test_dictionary will equal "well crap"
		# test_dictionary["foo"] = "well, oh boy!"		



if __name__ == '__main__':
    unittest.main()
