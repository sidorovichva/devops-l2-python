"""
12.Write a program with the following:
    a. Method that gets a number from the user (using input).
    b. Method that receives the number from the first method,
     and computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7)
"""


from utils import get_number


def sum_digits():
    return sum(int(digit) for digit in str(get_number()))


print(sum_digits())

