def greet():
    message = "Hello from inside the function"
    print(message)

greet()

# This would raise NameError:
# print(message)

# Global variables
course = "Artificial Intelligence"

def display_course():
    print("Learning:", course)

display_course()
print(course)

# global keyword
counter = 0

def increase_counter():
    global counter
    counter += 1

increase_counter()
increase_counter()

print(counter)

# Scope and nested functions
def outer():
    message = "Hello"

    def inner():
        nonlocal message
        message = "Updated message"

    inner()
    print(message)


outer()