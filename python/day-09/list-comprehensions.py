numbers = [1, 2, 3, 4, 5]

doubled = [number * 2 for number in numbers]
squares = [number ** 2 for number in numbers]
as_strings = [str(number) for number in numbers]

print("Doubled:", doubled)
print("Squares:", squares)
print("Strings:", as_strings)
