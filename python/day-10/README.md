# Day 10 — Python Functions

## Learning Objectives

- Define and call reusable functions.
- Understand parameters and arguments.
- Use positional and keyword arguments.
- Return values from functions.
- Use default parameters.
- Understand `*args` and `**kwargs`.
- Understand local and global scope.
- Write docstrings and type hints.
- Organize larger programs into smaller functions.
- Build a calculator and student management system.

## 1. Function Basics

A function is a reusable block of code.

```python
def greet():
    print("Hello!")

greet()
```

The `def` keyword defines a function. Calling the function executes its body.

## 2. Parameters and Arguments

Parameters are variables in a function definition. Arguments are values supplied when the function is called.

```python
def greet(name):
    print(f"Hello {name}")

greet("Sahil")
```

## 3. Return Values

`return` sends a result back to the caller. A function without an explicit return value returns `None`.

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

Functions can return multiple values, commonly packed into a tuple.

## 4. Default and Keyword Arguments

Default parameters provide values when arguments are omitted.

```python
def greet(name, message="Welcome!"):
    print(name, message)
```

Required parameters must come before parameters with default values. Keyword arguments identify parameters by name.

## 5. Variable Arguments

- `*args` collects extra positional arguments into a tuple.
- `**kwargs` collects extra keyword arguments into a dictionary.

These are useful when the number of inputs is not fixed.

## 6. Variable Scope

- Local variables are defined inside a function.
- Global variables are defined outside functions.
- `global` permits reassignment of a global variable inside a function.
- `nonlocal` permits reassignment of a variable in an enclosing function.

Prefer passing values through parameters and returning results over unnecessary global-state changes.

## 7. Docstrings and Type Hints

Docstrings describe a function's purpose. Type hints communicate intended parameter and return types, but Python does not enforce them automatically at runtime.

```python
def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b
```

## Main Programs

- `function-basics.py`
- `parameters-and-arguments.py`
- `return-statements.py`
- `default-and-keyword-arguments.py`
- `args-and-kwargs.py`
- `variable-scope.py`
- `docstrings-and-type-hints.py`
- `calculator-using-functions.py`
- `student-management-system.py`

## Exercises

1. Even or odd function.
2. Maximum of three numbers.
3. Factorial function.
4. List statistics function.
5. Function using `*args`.
6. Function using `**kwargs`.
7. Prime number function.

Store exercises in `exercises/`.

## Testing Checklist

- Test functions with valid and invalid inputs.
- Test functions with zero and negative numbers.
- Test empty collections.
- Test default arguments and keyword arguments.
- Test functions with no arguments for `*args`.
- Test functions with no keyword arguments for `**kwargs`.
- Confirm functions return the expected types and values.
- Confirm division by zero is handled safely.

## Connection to AI/ML

Functions will later organize data cleaning, feature engineering, model training, prediction, and evaluation. Reusable functions make machine learning code easier to test and maintain.

## Learning Resources

- [https://docs.python.org/3/tutorial/controlflow.html#defining-functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [https://www.youtube.com/@Coreyms](https://www.youtube.com/@Coreyms)
- [https://www.youtube.com/@freecodecamp](https://www.youtube.com/@freecodecamp)
- [https://nostarch.com/python-crash-course-3rd-edition](https://nostarch.com/python-crash-course-3rd-edition)

## Completion Checklist

- [x] Understand function definitions and calls.
- [x] Practise parameters and arguments.
- [x] Understand `return`.
- [x] Practise default and keyword arguments.
- [x] Understand `*args` and `**kwargs`.
- [x] Understand variable scope.
- [x] Write docstrings and type hints.
- [x] Complete the calculator project.
- [x] Complete the student management system.
- [x] Complete exercises 1–7.
- [x] Test edge cases.
- [x] Update the learning log.
- [x] Commit and push the Day 10 files.
- [x] Complete the Day 10 assessment.