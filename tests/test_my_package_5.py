import sys, os, math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import pytest
from my_package.main import get_sum, SumNumbers

def test_get_sum_positive():
    assert get_sum(2, 3) == 5
    assert get_sum(-2, 3) == 1
    assert get_sum(0, 0) == 0

def test_get_sum_negative():
    with pytest.raises(TypeError):
        get_sum('a', 3)
    with pytest.raises(TypeError):
        get_sum(2, 'b')

def test_sum_numbers_init_positive():
    sut = SumNumbers(2, 3)
    assert sut.a == 2
    assert sut.b == 3

def test_sum_numbers_init_negative():
    with pytest.raises(TypeError):
        SumNumbers('a', 3)
    with pytest.raises(TypeError):
        SumNumbers(2, 'b')

def test_sum_numbers_calculate_sum_positive():
    sut = SumNumbers(2, 3)
    assert sut.calculate_sum() == 5
    sut = SumNumbers(-2, 3)
    assert sut.calculate_sum() == 1
    sut = SumNumbers(0, 0)
    assert sut.calculate_sum() == 0

def test_sum_numbers_calculate_sum_negative():
    sut = SumNumbers(2, 3)
    with pytest.raises(TypeError):
        sut.calculate_sum = lambda: 'a'
        sut.calculate_sum()