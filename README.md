# Purpose

Pytest-xdist can obsure some leaky state issues in our tests. This repo explores some potential issues you can run into, and some solutions we may want to explore.

# Install

1. Create a virtual environment
2. Install dependencies from the requirements file
3. Run the command `pytest -n 2 --dist=loadscope` 
4. Then run `pytest -n 2 --dist=loadscope test_foo_bar_a.py test_foo_bar_b.py`
5. Now, run the test again, but this time run `pytest -n 2 --dist=loadscope test_foo_bar_b.py test_foo_bar_a.py` 
6. Now, repeat step 4, but uncomment out the forked decorators in `test_foo_bar_a.py`
7. Repeat step 5.
8. Observe, the state issues appear to be resolved.
