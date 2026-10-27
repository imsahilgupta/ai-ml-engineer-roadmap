# Day 7 — Python Lists and Collections

## Learning Objectives

- Create lists and access their elements.
- Use positive and negative indexing.
- Extract elements with slicing.
- Add, update, and remove values.
- Use list methods and built-in functions.
- Iterate over lists using loops and `enumerate()`.
- Calculate statistics from numerical data.
- Understand list references and copying.
- Build a student marks analyzer and shopping list manager.

## 1. List Basics

A list is an ordered, mutable collection.

```python
languages = ["Python", "Java", "JavaScript"]

print(languages[0])
print(languages[-1])
print(len(languages))
```

Positive indexing begins at zero. Negative indexing begins at `-1` for the final element.

## 2. Slicing

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[::2])
print(numbers[::-1])
```

The stop index is excluded.

## 3. Modify Lists

```python
fruits = ["apple", "banana"]

fruits.append("mango")
fruits.insert(1, "orange")
fruits.remove("banana")

print(fruits)
```

- `append()` adds one element.
- `extend()` adds elements from an iterable.
- `insert()` inserts at an index.
- `remove()` removes the first matching value.
- `pop()` removes and returns an element.
- `del` deletes an element or slice.

## 4. Useful Functions and Methods

- `len(items)`: number of elements.
- `sum(numbers)`: sum of numerical values.
- `min(numbers)`: smallest value.
- `max(numbers)`: largest value.
- `items.count(value)`: count matching values.
- `items.index(value)`: first matching index.
- `items.sort()`: sort the original list.
- `sorted(items)`: return a new sorted list.
- `items.reverse()`: reverse the original list order.

Handle empty lists before using `min()`, `max()`, or dividing by the list length.

## 5. Looping Through Lists

```python
scores = [70, 80, 90]

for index, score in enumerate(scores, start=1):
    print(f"Student {index}: {score}")
```

`enumerate()` provides an index and the corresponding element.

## 6. List References and Copies

```python
first = [1, 2, 3]
second = first.copy()
second.append(4)

print(first)
print(second)
```

Using `.copy()` creates a shallow copy. Assigning `second = first` instead makes both variables refer to the same list.

## 7. Practical Projects

### Student Marks Analyzer

File: `student-marks-analyzer.py`

- Store student marks.
- Calculate the total and average.
- Find the highest and lowest scores.
- Display pass/fail results using a practice threshold.

### Shopping List Manager

File: `shopping-list.py`

- Display the current list.
- Add an item.
- Remove an existing item.
- Validate empty input and invalid menu choices.
- Exit the program safely.

## 8. Exercises

1. Calculate list statistics and count even and odd values.
2. Remove duplicate values while preserving order.
3. Find the second-largest distinct number.
4. Reverse a list using three different approaches.
5. Search for a value and display matching indexes.

Store exercises in the `exercises/` directory.

## 9. Common Errors

- Accessing an invalid index.
- Removing a value that isn't present.
- Confusing `append()` and `extend()`.
- Assuming `sort()` returns a sorted list.
- Accidentally modifying the original list.
- Forgetting to handle empty lists.
- Confusing a list reference with an independent copy.

## 10. Connection to AI/ML

Lists provide a foundation for processing collections of data, calculating simple statistics, and understanding loops over records. Later, NumPy arrays and Pandas DataFrames will support more efficient numerical and tabular processing.

## 11. Learning Resources

- Python tutorial: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- Python data structures: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)
- Python built-in types: [https://docs.python.org/3/library/stdtypes.html](https://docs.python.org/3/library/stdtypes.html)
- Corey Schafer: [https://www.youtube.com/@Coreyms](https://www.youtube.com/@Coreyms)
- freeCodeCamp: [https://www.youtube.com/@freecodecamp](https://www.youtube.com/@freecodecamp)

## 12. Completion Checklist

- [x] Create and access lists.
- [x] Practise indexing and slicing.
- [x] Practise adding, updating, and removing elements.
- [x] Use list methods and built-in functions.
- [x] Loop through lists with `for` and `enumerate()`.
- [x] Complete the student marks analyzer.
- [x] Complete the shopping list manager.
- [x] Solve all five exercises.
- [x] Test empty lists and invalid values.
- [x] Update the learning log.
- [x] Review the README and code.
- [x] Commit and push changes to GitHub.
- [x] Pass the Day 7 assessment.