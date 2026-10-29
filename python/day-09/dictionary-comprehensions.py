numbers = [1, 2, 3, 4, 5]

squares = {number: number ** 2 for number in numbers}

print(squares)

print("*********")

scores = {
    "Asha": 85,
    "Ram": 32,
    "Mina": 91,
    "Sita": 45
}

passed = {
    name: score
    for name, score in scores.items()
    if score >= 40
}

print(passed)


print("*********")

countries = {
    "Nepal": "Kathmandu",
    "Japan": "Tokyo",
    "France": "Paris"
}

capitals = {
    capital: country
    for country, capital in countries.items()
}

print(capitals)

