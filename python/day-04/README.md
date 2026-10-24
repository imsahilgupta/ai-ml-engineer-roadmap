# Day 4 — Python Conditional Statements

## Learning Objectives

- Understand conditional statements and Boolean conditions.
- Use `if`, `elif`, and `else`.
- Combine conditions with `and`, `or`, and `not`.
- Write nested conditionals.
- Understand truthy and falsy values.
- Build decision-based programs.
- Test code, document learning, and publish changes to GitHub.

## 1. What Are Conditional Statements?

Conditional statements allow a program to choose which instructions to execute based on a condition.

A condition is an expression that evaluates to a truth value. Many conditions use comparison operators such as `==`, `!=`, `>`, `<`, `>=`, and `<=`.

Example:

```python
score = 65

if score >= 40:
    print("Pass")
else:
    print("Fail")
```

Because the score is at least 40, the program prints `Pass`.

## 2. The `if` Statement

An `if` statement executes its indented block only when the condition is true.

```python
age = 20

if age >= 18:
    print("Adult")
```

The colon begins the block, and indentation identifies the statements inside it. Four spaces are the standard indentation convention in Python.

## 3. The `if-else` Statement

Use `else` to specify what happens when the `if` condition is false.

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

The modulo operator calculates the remainder. An integer is even if dividing it by 2 leaves a remainder of zero.

## 4. The `if-elif-else` Statement

Use `elif` when multiple conditions must be checked in sequence.

```python
score = 82

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade F")
```

Python evaluates branches from top to bottom and executes only the first matching branch. Condition order is important.

## 5. Logical Operators in Conditions

- `and`: all combined conditions must be true.
- `or`: at least one combined condition must be true.
- `not`: reverses a truth value.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
```

Logical operators help express requirements involving multiple conditions.

## 6. Nested Conditions

A nested condition places one conditional inside another.

```python
age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Entry allowed")
    else:
        print("Ticket required")
else:
    print("Age requirement not met")
```

Indentation determines which block each statement belongs to.

## 7. Truthy and Falsy Values

Python conditions can evaluate values directly.

Common falsy values include `False`, `None`, numeric zero, empty strings, and empty collections. Most other values are truthy.

```python
username = ""

if username:
    print("Username provided")
else:
    print("Username is empty")
```

An empty string is falsy, but the non-empty string `"False"` is truthy.

## 8. Practical Programs

### Grade Calculator

Create `grade-calculator.py`. Ask for a score, validate that it is between 0 and 100, and display a grade using an ordered conditional chain.

### Eligibility Checker

Create `eligibility-checker.py`. Ask for age and whether the user meets an example qualification. Use logical operators and conditional branches to display the outcome.

### Nested Conditions

Create `nested-conditions.py`. Check a username first and a password second. This is a learning exercise only, not a secure authentication system.

## 9. Exercises

1. **Number classifier:** Determine whether an integer is positive, negative, or zero, and whether it is even or odd.
2. **Exam result:** Validate a score between 0 and 100 and display Pass for a score of at least 40, otherwise Fail.
3. **Shopping discount:** Apply a 10% discount when the subtotal is at least 1,000.
4. **Scholarship screening practice:** Validate score and attendance values from 0 to 100. Qualify the example applicant only when the score is at least 80 and attendance is at least 90%.

Test normal, failing, and boundary cases.

## 10. Common Errors

- Forgetting the colon after a conditional header.
- Using `=` instead of `==` in a comparison.
- Incorrect indentation.
- Placing broad conditions before more specific conditions.
- Assuming that a non-empty string containing `"False"` is falsy.
- Failing to validate user input before converting or processing it.

## 11. Connection to AI/ML

Conditional statements are used to validate data, apply business rules, handle errors, select program behaviour, and check model evaluation thresholds.

They do not replace machine-learning models. They are part of the programming logic used to build reliable AI applications.

## 12. Learning Resources

- Python Tutorial: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- Python compound statements: [https://docs.python.org/3/reference/compound_stmts.html](https://docs.python.org/3/reference/compound_stmts.html)
- Corey Schafer Python tutorials: [https://www.youtube.com/@Coreyms](https://www.youtube.com/@Coreyms)
- freeCodeCamp: [https://www.youtube.com/@freecodecamp](https://www.youtube.com/@freecodecamp)

## 13. Completion Checklist

- [x] Understand `if`, `elif`, and `else`.
- [x] Understand indentation and code blocks.
- [x] Practise conditions with comparison operators.
- [x] Combine conditions using `and`, `or`, and `not`.
- [x] Complete the grade calculator.
- [x] Complete the eligibility checker.
- [x] Complete all four exercises.
- [x] Test normal and boundary cases.
- [x] Update the learning log.
- [x] Review and save this README.
- [x] Commit and push changes to GitHub.
- [x] Complete the Day 4 assessment.