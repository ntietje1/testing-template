# test_simple_methods.py

import pytest
from simple_methods import add, subtract, multiply, divide, square

def test_add():
    assert add(3, 4) == 7

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(10, 2) == 5

def test_square():
    # This test will fail deliberately (expected result is wrong)
    assert square(5) == 20  # Should be 25, not 20

