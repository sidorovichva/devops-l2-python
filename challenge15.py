"""
15.Write a program to accept a number from a user and calculate the sum of all numbers
from 1 to a given number
For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
Expected Output:
    Enter number 10
    Sum is: 55
"""

from utils import get_number


def sum_numbers(x) -> int:
    number: int = x
    return sum(range(1, number + 1))


print(sum_numbers(get_number()))
