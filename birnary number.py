def binary_to_decimal(binary_number):
    decimal_number = 0
    binary_digits = list(binary_number)
    binary_digits.reverse()
    
    for i in range(len(binary_digits)):
        digit = int(binary_digits[i])
        if digit != 0 and digit != 1:
            raise ValueError("Invalid binary number")
        decimal_number += digit * (2 ** i)
    
    return decimal_number

binary_number = input("Enter a binary number: ")
try:
    decimal_equivalent = binary_to_decimal(binary_number)
    print(f"The decimal equivalent of {binary_number} is: {decimal_equivalent}")
except ValueError as e:
    print(str(e))