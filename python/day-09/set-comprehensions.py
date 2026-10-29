numbers = [1, 2, 2, 3, 3, 4, 5, 5]

unique_squares = {number ** 2 for number in numbers}
even_numbers = {number for number in numbers if number % 2 == 0}

print("Unique squares:", unique_squares)
print("Even numbers:", even_numbers)
