#simpleProgram/caculator.py
from typing import Union, Optional
class Calculator:
    """Simple calculator class for basic arithmetic operations."""
    def add(self, a: float, b: float) -> float:
        """Add two numbers together."""
        return a + b
    def subtract(self, a: float, b: float) -> float:
        """Subtract one number from another."""
        return a - b
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers together."""
        return a * b
    def divide(self, a: float, b: Optional[float]) -> Union[float, None]:
        """Divide one number by another. Returns None for division by zero."""
        if b == 0:
            return None
        else:
            return a / b
def main() -> None:
    """Main entry point to demonstrate usage of the Calculator class."""
    calculator = Calculator()
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, * or /): ")
            if op in ["+", "-", "*"]:
                num2 = float(input("Enter second number: "))
                result = {
                    "+": lambda: calculator.add(num1, num2),
                    "-": lambda: calculator.subtract(num1, num2),
                    "*": lambda: calculator.multiply(num1, num2)
                }[op]()
            elif op == "/":
                num2 = float(input("Enter second number: "))
                result = calculator.divide(num1, num2)
            else:
                raise ValueError(f"Invalid operator: {op}")
            print(f"Result: {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {str(e)}")
        finally:
            cont = input("Continue? (y/n): ")
            if cont.lower() != "y":
                break
if __name__ == "__main__":
    main()