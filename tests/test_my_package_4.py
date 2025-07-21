import sys, os, math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import pytest
from my_package.main import get_sum, SumNumbers

def test_get_sum_positive():
    assert get_sum(2, 3) == 5

def test_get_sum_negative():
    assert get_sum(-2, 3) == 1

def test_get_sum_zero():
    assert get_sum(0, 0) == 0

def test_get_sum_float_input():
    with pytest.raises(TypeError):
        get_sum(2.5, 3)

def test_sum_numbers_init():
    sum_obj = SumNumbers(2, 3)
    assert sum_obj.a == 2
    assert sum_obj.b == 3

def test_sum_numbers_calculate_sum_positive():
    sum_obj = SumNumbers(2, 3)
    assert sum_obj.calculate_sum() == 5

def test_sum_numbers_calculate_sum_negative():
    sum_obj = SumNumbers(-2, 3)
    assert sum_obj.calculate_sum() == 1

def test_sum_numbers_calculate_sum_zero():
    sum_obj = SumNumbers(0, 0)
    assert sum_obj.calculate_sum() == 0

def test_sum_numbers_calculate_sum_float_input():
    with pytest.raises(TypeError):
        sum_obj = SumNumbers(2.5, 3)
        sum_obj.calculate_sum()