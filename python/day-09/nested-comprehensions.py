# A. Generate coordinate pairs
pairs = [
    (x, y)
    for x in range(1, 4)
    for y in range(1, 3)
]

print(pairs)

# B. Flatten a nested list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    number
    for row in matrix
    for number in row
]

print(flattened)
