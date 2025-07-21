import math
from typing import Optional, Union

import pytest

from src.simpleProgram.caculator import Calculator


#from my_package.main import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (1.0, 2.0, 3.0),
    (10.0, -5.0, 5.0),
    (0.0, 0.0, 0.0)
])
def test_add(sut: Calculator, a: float, b: float, expected: float) -> None:
    assert math.isclose(sut.add(a, b), expected)

@pytest.mark.parametrize("a, b, expected", [
    (1.0, 2.0, -1.0),
    (10.0, -5.0, 15.0),
    (-10.0, 5.0, -15.0)
])
def test_subtract(sut: Calculator, a: float, b: float, expected: float) -> None:
    assert math.isclose(sut.subtract(a, b), expected)

@pytest.mark.parametrize("a, b, expected", [
    (1.0, 2.0, 2.0),
    (10.0, -5.0, -50.0),
    (-10.0, 5.0, -50.0)
])
def test_multiply(sut: Calculator, a: float, b: float, expected: float) -> None:
    assert math.isclose(sut.multiply(a, b), expected)

@pytest.mark.parametrize("a, b, expected", [
    (2.0, 1.0, 2.0),
    (-5.0, -10.0, 0.5),
    (0.0, 2.0, float('inf'))
])
def test_divide(sut: Calculator, a: float, b: Optional[float], expected: Union[float, None]) -> None:
    if b == 0.0 or b is None:
        assert math.isnan(sut.divide(a, b))
    else:
        assert math.isclose(sut.divide(a, b), expected)