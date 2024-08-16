def get_number() -> int:
    while True:
        inp = input("Enter an integer number: ")
        try:
            number = int(inp)
            return number
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
