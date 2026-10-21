# Day 2 — Python Variables and Data Types

## 1. Learning Objectives

By the end of this lesson, I should be able to:

- Define variables and explain assignment.
- Follow Python variable-naming conventions.
- Recognize `str`, `int`, `float`, `bool`, and `NoneType`.
- Inspect values using `type()`.
- Convert compatible values using `str()`, `int()`, `float()`, and `bool()`.
- Collect text input with `input()`.
- Explain why `input()` returns a string.
- Format output using f-strings.
- Build a simple student-profile program.
- Commit and push the completed lesson to GitHub.

## 2. What Is a Variable?

A variable is a name that refers to a value in a program. It allows information to be stored and reused.

```python
student_name = "Sahil"
age = 22
is_learning_python = True

print(student_name)
print(age)
print(is_learning_python)
```

The values in this example are illustrative and can be changed.

### Assignment

In `student_name = "Sahil"`:

- `student_name` is the variable name.
- `=` is the assignment operator.
- `"Sahil"` is the assigned string value.

Assignment associates a value with a name. It is not the same as checking equality, which we will study later.

### Naming Rules and Conventions

Valid examples:

```python
student_name = "Sahil"
total_marks = 450
study_hours = 2.5
```

Variable names cannot start with a digit, contain spaces, or use Python reserved keywords.

```python
# 2name = "Sahil"  # Invalid: starts with a digit
# student age = 22  # Invalid: contains a space
# class = "BCA"     # Invalid: reserved keyword
```

Python is case-sensitive. `name` and `Name` are different variables.

Use `snake_case` for ordinary variable names because it is the standard Python convention.

## 3. What Is a Data Type?

A data type identifies the kind of value a variable refers to. Different types support different operations.

### String — `str`

A string represents text and is written inside quotes.

```python
student_name = "Sahil"
language = "Python"

print(type(student_name))
```

Strings are useful for names, labels, messages, and textual data.

### Integer — `int`

An integer represents a whole number without a decimal part.

```python
age = 22
total_students = 150

print(type(age))
```

Integers are useful for counts and whole-number quantities.

### Float — `float`

A float represents a floating-point number.

```python
height = 1.70
accuracy = 0.95

print(type(height))
```

Floats are useful for measurements and numerical calculations. Floating-point arithmetic can have small precision limitations.

### Boolean — `bool`

A Boolean represents one of two values: `True` or `False`.

```python
is_enrolled = True
has_finished_lesson = False

print(type(is_enrolled))
```

Boolean values are commonly used in conditions and status checks.

### None — `NoneType`

`None` represents the absence of a value.

```python
result = None

print(result)
print(type(result))
```

It is not the same as zero, an empty string, or `False`.

### Other Types

Python also provides collection types, including:

- `list`
- `tuple`
- `dict`
- `set`

These will be covered in later lessons.

## 4. Inspecting Types with `type()`

The built-in `type()` function identifies the type of an object.

```python
name = "Sahil"
age = 22
height = 1.70
is_student = True
result = None

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(result))
```

Expected type names are `str`, `int`, `float`, `bool`, and `NoneType`, respectively.

Knowing the types of values is important when processing datasets, validating input, and preparing data for machine-learning models.

## 5. Type Conversion

Type conversion changes a value into another compatible type.

```python
age_text = "22"
age_number = int(age_text)
age_decimal = float(age_text)
age_string = str(age_number)

print(age_number, type(age_number))
print(age_decimal, type(age_decimal))
print(age_string, type(age_string))
```

Common conversion functions:

- `str(value)` — creates a string representation.
- `int(value)` — converts a compatible value to an integer.
- `float(value)` — converts a compatible value to a float.
- `bool(value)` — converts a value to a Boolean.

Examples:

```python
print(int("25"))
print(float("3.5"))
print(str(100))
print(bool(1))
```

### Conversion Errors

This succeeds:

```python
age = int("22")
```

This raises a `ValueError`:

```python
# age = int("twenty-two")
```

The text is not a valid integer representation.

A non-empty string is truthy, even when its content is `"False"`:

```python
print(bool(""))
print(bool("False"))
```

The results are `False` and `True`. Boolean conversion checks whether a value is truthy; it does not interpret the meaning of words.

## 6. User Input

The `input()` function collects text entered by a user.

```python
name = input("Enter your name: ")
print("Welcome,", name)
```

**Important:** `input()` returns a string, even if the user types digits.

```python
age_text = input("Enter your age: ")
print(type(age_text))
```

To use the age in numerical calculations, convert it:

```python
age = int(input("Enter your age: "))
next_year_age = age + 1

print(next_year_age)
```

This example expects a whole number. Invalid input causes an error until validation is added.

## 7. F-Strings

F-strings insert values into text using expressions inside curly braces.

```python
name = "Sahil"
day = 2
topic = "variables and data types"

print(f"My name is {name}.")
print(f"Today is Day {day}.")
print(f"I am studying {topic}.")
```

F-strings make output easier to read and maintain.

They can also format numbers:

```python
accuracy = 0.95678
print(f"Accuracy: {accuracy:.2%}")
```

Output:

```text
Accuracy: 95.68%
```

The `.2%` format displays a percentage with two decimal places.

## 8. Practical Project: Student Profile

```python
student_name = input("Enter your name: ")
education = input("Enter your education: ")
career_goal = input("Enter your career goal: ")
study_hours = float(input("Hours studied today: "))

print("\n--- Student Profile ---")
print(f"Name: {student_name}")
print(f"Education: {education}")
print(f"Career goal: {career_goal}")
print(f"Study hours today: {study_hours:.1f}")

print("\n--- Data Types ---")
print(f"student_name: {type(student_name).__name__}")
print(f"education: {type(education).__name__}")
print(f"career_goal: {type(career_goal).__name__}")
print(f"study_hours: {type(study_hours).__name__}")
```

Run it from the repository root:

`python python/day-02/student-profile.py`

This project combines variables, input, conversion, f-strings, and type inspection.

It expects numeric input for study hours. Invalid numeric input will raise an error; input validation will be studied later.

## 9. Connection to AI and Machine Learning

Data types matter in AI/ML because data must be represented and processed appropriately.

Examples:

- Text data can contain names, reviews, or documents.
- Integer values can represent counts or encoded categories.
- Floating-point values can represent measurements and model scores.
- Boolean values can represent flags or conditions.

Real datasets also contain missing values, inconsistent formats, and unexpected input. Learning Python types is an early step toward data cleaning and reliable model pipelines.

Python types alone do not determine how every machine-learning library stores data. Libraries such as NumPy and Pandas provide additional data structures and rules that we will study later.

## 10. Exercises

### Exercise 1 — Personal Introduction

Create `exercises/exercise-01.py`.

Store and display:

- Your name.
- Your education.
- Your career goal.
- Your favorite programming language.
- Whether you are learning AI/ML.

Use at least one string, one Boolean, and one integer or float.

### Exercise 2 — Type Explorer

Create `exercises/exercise-02.py`.

1. Create one variable of each type: `str`, `int`, `float`, `bool`, and `NoneType`.
2. Print each variable.
3. Print each variable's type.
4. Explain the output in your learning log.

### Exercise 3 — Simple Calculator Input

Create `exercises/exercise-03.py`.

1. Ask the user for two numbers.
2. Convert both inputs to floats.
3. Display their sum, difference, product, and quotient.

## 11. Troubleshooting

### `ValueError`

The entered value could not be converted to the requested type. Check the input format.

### Unexpected string concatenation

Remember that `input()` returns a string. Convert numeric input before performing arithmetic.

### `TypeError`

Check whether the operation supports the types being used.

### Variable not defined

Check spelling, capitalization, and whether the variable was assigned before it was used.

### Incorrect f-string output

Confirm that the string begins with `f` and that variable names are inside `{}`.

## 12. Learning Resources

- Python Tutorial: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- Python built-in types: [https://docs.python.org/3/library/stdtypes.html](https://docs.python.org/3/library/stdtypes.html)
- Built-in functions, including `type()`, `input()`, and conversion functions: [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)
- Python for Beginners: [https://www.youtube.com/@Coreyms](https://www.youtube.com/@Coreyms)

Read the relevant sections and run the examples yourself rather than only watching or reading.

## 13. Key Takeaways

- Variables provide names for values.
- Python variable names are case-sensitive.
- `str`, `int`, `float`, `bool`, and `NoneType` represent different kinds of values.
- `type()` identifies an object's type.
- Conversion functions work only for compatible values.
- `input()` returns a string.
- F-strings provide readable output formatting.
- Understanding data types helps prepare for data processing and AI/ML.

## 14. Completion Checklist

- [x] Variables created and explained.
- [x] Variable naming rules understood.
- [x] Five main types practiced.
- [x] `type()` used successfully.
- [x] Type conversion practiced.
- [x] User input tested.
- [x] F-strings practiced.
- [x] Student-profile program completed.
- [x] All three exercises completed.
- [x] Learning log updated.
- [x] README saved in `python/day-02/`.
- [x] Changes committed and pushed to GitHub.
- [x] LinkedIn post edited to match actual work.
- [x] Day 2 assessment passed.