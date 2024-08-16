"""
16.Print list in reverse order using a loop
Given: list1 = [10, 20, 30, 40, 50]
Expected output:
    50
    40
    30
    20
    10
"""

list1 = [10, 20, 30, 40, 50]
[print(i) for i in list1[::-1]]
