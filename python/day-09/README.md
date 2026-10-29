# Day 9 — Python Comprehensions

## Learning Objectives

- Understand list, set, and dictionary comprehensions.
- Transform data in a concise, readable way.
- Filter values using conditions.
- Use conditional expressions inside comprehensions.
- Flatten nested collections.
- Process dictionaries using `.items()`.
- Apply comprehensions to basic data-cleaning tasks.
- Recognize when regular loops are clearer.

## 1. List Comprehensions

General syntax:

```python
[expression for item in iterable]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
```

Filter elements:

```python
evens = [number for number in numbers if number % 2 == 0]
```

Choose an output for each element:

```python
labels = [
    "even" if number % 2 == 0 else "odd"
    for number in numbers
]
```

## 2. Set Comprehensions

General syntax:

```python
{expression for item in iterable}
```

Set comprehensions produce unique elements and do not preserve a guaranteed display order.

## 3. Dictionary Comprehensions

General syntax:

```python
{key_expression: value_expression for item in iterable}
```

Example:

```python
squares = {number: number ** 2 for number in range(1, 6)}
```

Use `.items()` to iterate through existing key-value pairs. Remember that repeated generated keys overwrite earlier values.

## 4. Nested Comprehensions

Nested comprehensions can flatten nested lists or generate combinations.

```python
matrix = [[1, 2], [3, 4]]
flattened = [number for row in matrix for number in row]
```

Use regular loops when nested comprehensions become difficult to read.

## Programs

- `list-comprehensions.py`
- `set-comprehensions.py`
- `dictionary-comprehensions.py`
- `nested-comprehensions.py`
- `student-scores-analyzer.py`
- Optional: `data-cleaning.py`

## Exercises

1. Generate squares and cubes.
2. Filter positive numbers.
3. Find unique word lengths.
4. Filter and discount product prices.
5. Flatten a matrix.
6. Generate student pass/fail reports.

Store the six exercise files in `exercises/`.

## Testing Checklist

- Test empty lists and dictionaries.
- Test collections containing duplicate values.
- Check the results of filtering conditions.
- Test values at the boundary of a condition.
- Handle empty filtered results before calculating averages.
- Check whether generated dictionary keys can repeat.
- Compare comprehension results with equivalent loop implementations.

## Connection to AI/ML

Comprehensions can help transform records, filter values, normalize simple data, and build mappings. These are useful foundations for data preparation. For large datasets, specialized libraries such as NumPy and Pandas may be more appropriate.

## Learning Resources

- [https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [https://docs.python.org/3/reference/expressions.html](https://docs.python.org/3/reference/expressions.html)
- [https://www.youtube.com/@Coreyms](https://www.youtube.com/@Coreyms)
- [https://www.youtube.com/@freecodecamp](https://www.youtube.com/@freecodecamp)
- [https://automatetheboringstuff.com/](https://automatetheboringstuff.com/)

## Completion Checklist

- [x] Understand list comprehensions.
- [x] Practise filtering and conditional expressions.
- [x] Understand set comprehensions.
- [x] Understand dictionary comprehensions.
- [x] Flatten a nested list.
- [x] Complete the student scores analyzer.
- [x] Complete exercises 1–6.
- [x] Test edge cases.
- [x] Update `notes/learning-log.md`.
- [x] Review code and README.
- [x] Commit and push the Day 9 files.
- [x] Complete the Day 9 assessment.