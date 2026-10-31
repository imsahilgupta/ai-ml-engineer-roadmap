def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

print(calculate_area(10, 5))
print(calculate_area.__doc__)

# type hints
def calculate_area(length: float, width: float) -> float:
    """Return the area of a rectangle."""
    return length * width

area = calculate_area(10.5, 5.0)
print(area)

# Validate function inputs
def calculate_average(numbers: list[float]) -> float | None:
    """Return the average, or None if the list is empty."""
    if not numbers:
        return None

    return sum(numbers) / len(numbers)

print(calculate_average([70, 80, 90]))
print(calculate_average([]))