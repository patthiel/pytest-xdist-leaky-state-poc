import pytest
from test import test_dictionary

# @pytest.mark.forked
class TestFooBarA:
	def test_foo_bar(self):
		assert test_dictionary["foo"] == "bar"
		test_dictionary["foo"] = "Oh no!"

# @pytest.mark.forked
class TestFooBarB:
	def test_oh_no(self):
		# This should fail because test dictionary = "ohno"
		assert test_dictionary["foo"] == "bar"
		test_dictionary["foo"] = "Heck yeah"

