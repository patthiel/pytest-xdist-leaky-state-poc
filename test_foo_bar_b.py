import pytest
from test import test_dictionary

class TestFooBarC:
	def test_well_shit(self):
		assert test_dictionary["foo"] == "bar"
		# After the test, let's do something rude to our variable:
		# test_dictionary["foo"] = "well, crap..."

class TestFooBarD:
	def test_oh_boy(self):
		assert test_dictionary["foo"] == "bar"
		# After this one let's do that too:
		# This should fail because test_dictionary will equal "well crap"
		# test_dictionary["foo"] = "well, oh boy!"		

