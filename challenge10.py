"""
10.Create a nested for loop (loop inside another loop) to create a pyramid shape:
"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print("#", end='')
    print()
