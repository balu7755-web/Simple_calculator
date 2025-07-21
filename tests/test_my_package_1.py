import pytest
from simpleProgram.caculator import Calculator

def test_add():
    calculator = Calculator()
    assert math.isclose(calculator.add(2.0, 3.0), 5.0)

def test_subtract():
    calculator = Calculator()
    assert math.isclose(calculator.subtract(4.0, 1.0), 3.0)

def test_multiply():
    calculator = Calculator()
    assert math.isclose(calculator.multiply(2.0, 3.0), 6.0)

def test_divide_valid():
    calculator = Calculator()
    assert math.isclose(calculator.divide(4.0, 2.0), 2.0)

def test_divide_zero():
    calculator = Calculator()
    result = calculator.divide(4.0, 0.0)
    assert math.isnan(result)

def test_divide_invalid_operator():
    with pytest.raises(ValueError):
        calculator = Calculator()
        calculator.divide(4.0, 1.0, "invalid operator")

def test_main_valid_input():
    with pytest.raises(SystemExit) as e:
        main()
    assert e.type == SystemExit
    assert e.status == 0

def test_main_invalid_operator():
    with pytest.raises(ValueError):
        main("invalid operator")