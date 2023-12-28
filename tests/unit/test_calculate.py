"""
Python code to perform mathematical operations on two variable
"""

def summation(num1: int, num2: int) -> int:
    """
    Calculate the summation of two number
    """
    return num1 + num2

def subtraction(num1: int, num2: int) -> int:
    """
    Calculate the subtraction of two number
    """
    return num1 - num2

def multiplication(num1: int, num2: int) -> int:
    """
    Calculate the multiplication of two number
    """
    return num1 * num2

def division(num1: int, num2: int) -> float:
    """
    Calculate the division of two number
    """
    return num1 / num2

def test_increment():
    assert multiplication(2, 2) == 4

# This test is designed to fail for demonstration purposes.
def test_decrement():
    assert subtraction(5, 1) == 4