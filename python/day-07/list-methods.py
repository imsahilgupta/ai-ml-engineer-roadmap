fruits = ["apple", "banana"]

fruits.append("mango")
fruits.insert(1, "orange")
fruits.remove("banana")

print(fruits)

print("********")

scores = [78, 92, 65, 92, 84]

print("Count:", len(scores))
print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Total:", sum(scores))
print("Number of 92s:", scores.count(92))

scores.sort()
print("Sorted:", scores)