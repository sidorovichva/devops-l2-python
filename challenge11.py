"""
11.Create a nested for loop to create X shape (width is 7, length is 7):
"""

for i in range(1, 8):
    for j in range(1, 8):
        if j == i or j == 8 - i:
            print("#", end='')
        else:
            print(" ", end='')
    print()
