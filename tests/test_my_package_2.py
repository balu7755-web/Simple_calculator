import pytest
from my_package.calculator import Calculator

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1.0, 2.0, 3.0),
        (-1.0, 1.0, 0.0),
        (0.0, 0.0, 0.0)
    ]
)
def test_add(sut: Calculator, a: float, b: float, expected: float):
    assert math.isclose(sut.add(a, b), expected)

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1.0, 2.0, -1.0),
        (-1.0, 1.0, -3.0),
        (0.0, 1.0, -1.0)
    ]
)
def test_subtract(sut: Calculator, a: float, b: float, expected: float):
    assert math.isclose(sut.subtract(a, b), expected)

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1.0, 2.0, 2.0),
        (-1.0, -1.0, 1.0),
        (0.0, 1.0, 0.0)
    ]
)
def test_multiply(sut: Calculator, a: float, b: float, expected: float):
    assert math.isclose(sut.multiply(a, b), expected)

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2.0, 1.0, 2.0),
        (-1.0, -1.0, -1.0),
        (0.0, 1.0, float('inf'))
    ]
)
def test_divide(sut: Calculator, a: float, b: float, expected: object):
    if math.isclose(b, 0.0) or math.isnan(a / b):
        assert sut.divide(a, b) is None
    else:
        assert math.isclose(sut.divide(a, b), expected)