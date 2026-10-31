# args
def calculate_sum(*args):
    print("Received values:", args)
    print("Type:", type(args))

    total = sum(args)
    return total

print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30))
print(calculate_sum(1, 2, 3, 4, 5))

# kwargs
def display_profile(**kwargs):
    print("Profile information:")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

# both together
display_profile(
    name="Sahil",
    course="BCA",
    skill="Python",
    goal="AI/ML Engineer"
)

def show_data(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)


show_data(10, 20, 30, name="Asha", age=22)