# Day 8 — Python Tuples, Sets, and Dictionaries

## Learning Objectives

- Explain the differences between lists, tuples, sets, and dictionaries.
- Create, access, and unpack tuples.
- Understand tuple immutability.
- Create sets and remove duplicate values.
- Perform union, intersection, difference, and symmetric difference.
- Create, read, update, and delete dictionary entries.
- Iterate through dictionaries using `items()`.
- Build a student record manager.
- Count word and character frequencies.
- Write readable, tested Python programs.

## Concepts

### Tuples

Tuples are ordered and immutable. Use indexing, slicing, `len()`, `count()`, `index()`, and unpacking.

```python
student = ("Alex", 21, "BCA")
name, age, degree = student
```

A single-element tuple requires a trailing comma: `(5,)`.

### Sets

Sets store unique, hashable elements and do not support indexing.

- `A | B`: union
- `A & B`: intersection
- `A - B`: difference
- `A ^ B`: symmetric difference
- `add()`: add an element
- `discard()`: remove an element safely if present

Use `set()` to create an empty set.

### Dictionaries

Dictionaries map unique, hashable keys to values.

- `data[key]`: access a value
- `data.get(key, default)`: access safely with a default
- `data[key] = value`: add or update
- `data.pop(key)`: remove a key and return its value
- `data.keys()`: access keys
- `data.values()`: access values
- `data.items()`: iterate through key-value pairs

## Programs

- `tuple-basics.py`
- `set-basics.py`
- `dictionary-basics.py`
- `student-record-manager.py`
- `word-frequency-counter.py`

## Exercises

1. Tuple unpacking and variable swapping.
2. Remove duplicate numbers.
3. Compare two sets of interests.
4. Create and search a dictionary of books.
5. Analyze student marks and handle empty data.
6. Count character frequencies.

Store the exercise files in `exercises/`.

## Testing Checklist

- Test an empty set and an empty dictionary.
- Test a dictionary lookup with a missing key.
- Test removal of an absent set element.
- Test tuples with one element.
- Test repeated values and empty text.
- Avoid calling `min()`, `max()`, or dividing by length without handling empty collections.
- Confirm that program output matches expected results.

## Connection to AI/ML

Tuples, sets, and dictionaries support structured data representation, deduplication, lookups, and frequency counting. These concepts prepare you for processing datasets and working with APIs, Pandas, and machine learning workflows.

## Learning Resources

- Python data structures: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)
- Python built-in types: [https://docs.python.org/3/library/stdtypes.html](https://docs.python.org/3/library/stdtypes.html)
- Corey Schafer: [https://www.youtube.com/@Coreyms](https://www.youtube.com/@Coreyms)
- freeCodeCamp: [https://www.youtube.com/@freecodecamp](https://www.youtube.com/@freecodecamp)
- Automate the Boring Stuff: [https://automatetheboringstuff.com/](https://automatetheboringstuff.com/)

## Completion Checklist

- [x] Understand tuples and unpacking.
- [x] Understand set uniqueness and set operations.
- [x] Understand dictionary keys and values.
- [x] Complete all five main programs.
- [x] Complete exercises 1–6.
- [x] Test edge cases and invalid input.
- [x] Update `notes/learning-log.md`.
- [x] Review code and README.
- [x] Commit and push the Day 8 files.
- [x] Complete the Day 8 assessment.