# Creating tuples
coordinates = (10, 20)
rgb_color = (255, 128, 0)
student = ("Alex", 21, "BCA")

# Accessing elements
print("First coordinate:", coordinates[0])
print("Student name:", student[0])
print("Last student value:", student[-1])

# Tuple length and counting
print("Number of student fields:", len(student))
print("Number of 20s:", (10, 20, 20, 30).count(20))

# Finding an element
print("Index of 128:", rgb_color.index(128))

# A one-item tuple needs a comma
single_item = (5,)
print("Single-item tuple:", single_item)
print("Its type:", type(single_item))
