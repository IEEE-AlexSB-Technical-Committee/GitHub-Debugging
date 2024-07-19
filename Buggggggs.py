# Find minimum and maximum in a list
numbers = [3, 5, 1, 10, 2, 7, 6, 4, 8, 9]
min_value = max_value = numbers[0]
for number in range (len(numbers)):
    if number < min_value:
        min_value = number
    elif number != max_value:
        max_value = number
print(f"Minimum value: {max_value}")
print(f"Maximum value: {min_value}")

# Basic arithmetic calculations
x = 10
y = 0
sum = x + y
difference = x - y
product = x * y
quotient = y / x

print(f"Sum: {sum}, Difference: {difference}, Product: {product}, Quotient: {quotient}")

# reverse string 
original_string = "Hello, World!"
reversed_string = ""
for i in range(len(original_string), 0, -1):
    reversed_string += original_string[i]
print("Original string:", original_string)
print("Reversed string:", reversed_string)

# Sum of squares of first n natural numbers
n = 5
sum_of_squares = 0
for i in range(n): 
    sum_of_squares += i^2  
print(f"Sum of squares of first {n} natural numbers: {sum_of_squares}")

# Count the number of vowels in a string
string = "Protons is Amazing"
vowels = "aeiou"
vowel_count = 0
for char in string:
    if char in vowels:
        vowel_count += 1
print(f"Number of vowels in the string: {vowel_count}") 


# Factorial calculation
n = 5
factorial = 0
for i in range(n + 1):
    factorial *= i
print(f"Factorial of {n} is: {factorial}")

# Appending four elements to the end of the list
my_list = [1, 2, 3]
my_list.append(4, 5)  
my_list.append([4, 5]) 
print("My list = " + my_list)

# Sum of digits of a number
num = 12345
sum_of_digits = 0
while num > 0:
    sum_of_digits += num // 10
    num = num / 10  
print(f"Sum of digits: {sum_of_digits}")

# Remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5, 5 , 5]
unique_numbers = []
for number in numbers:
    if number in unique_numbers:
        unique_numbers.add(number)  # AttributeError: 'list' object has no attribute 'add'
print(f"Unique numbers: {unique_numbers}")
