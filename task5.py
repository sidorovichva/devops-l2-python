"""
5. Write a program with variables holding the following
    a. Your age.
    b. First letter of your last name.
    c. Current shekels-dollar currency.
    d. Did you fly abroad (true/false)?
    e. Your apartment numbers.
    f. Print all variables.
    g. Add the currency to your age and check the result.
"""

age = 70
last_name = 'S'
currency = 3.5
abroad = False
apartment = 5

print(f"age: {age}")
print(f"last_name: {last_name}")
print(f"currency: {currency}")
print(f"abroad: {abroad}")
print(f"apartment: {apartment}")

age = age + currency
print(f"age: {age}")
