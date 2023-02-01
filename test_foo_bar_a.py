import unittest
from test import test_dictionary

# @pytest.mark.forked
class TestFooBarA(unittest.TestCase):
	def test_foo_bar(self):
		self.assertEqual(test_dictionary["foo"], "bar")
		test_dictionary["foo"] = "Oh no!"

# @pytest.mark.forked
class TestFooBarB(unittest.TestCase):
	def test_oh_no(self):
		# This should fail because test dictionary = "ohno"
		assertEqual(test_dictionary["foo"], "bar")
		test_dictionary["foo"] = "Heck yeah"


if __name__ == '__main__':
    unittest.main()
