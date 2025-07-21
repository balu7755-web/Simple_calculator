simpleProgram/__init__.py
# empty file
simpleProgram/sum_numbers.py
def get_sum(a: int, b: int) -> int:
    """
    Calculate the sum of two numbers.
    Args:
    a (int): The first number.
    b (int): The second number.
    Returns:
    int: The sum of a and b.
    """
    return a + b
class SumNumbers:
    """
    A class to calculate the sum of two numbers.
    """
    def __init__(self, a: int, b: int):
        """
        Initialize the class with two numbers.
        Args:
        a (int): The first number.
        b (int): The second number.
        """
        self.a = a
        self.b = b
    def calculate_sum(self) -> int:
        """
        Calculate the sum of the two numbers.
        Returns:
        int: The sum of a and b.
        """
        return get_sum(self.a, self.b)
if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        sum_obj = SumNumbers(num1, num2)
        result = sum_obj.calculate_sum()
        print(f"The sum of {num1} and {num2} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")