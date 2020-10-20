# import pytest
import pytest

# import the function from your file
from session11 import add_numbers

# Check if properly adds positive numbers
def test_add_positive():
    assert add_numbers(1,2) == 3