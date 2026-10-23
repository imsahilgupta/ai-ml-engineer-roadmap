# Day 3 — Python Operators and Expressions

## 1. Learning Objectives

By the end of this lesson, I should be able to:

- Explain operators, operands, and expressions.
- Use arithmetic operators.
- Compare values using comparison operators.
- Combine Boolean conditions using logical operators.
- Update variables with assignment operators.
- Understand basic operator precedence.
- Recognize membership and identity operators.
- Build a simple calculator.
- Test exercises and publish my work to GitHub.

## 2. Operators and Expressions

An operator performs an operation on values. The values involved are called operands.

An expression is code that Python evaluates to produce a value.

```python
total = 10 + 5
print(total)
```

Here, `10` and `5` are operands, `+` is an operator, and `10 + 5` evaluates to `15`.

## 3. Arithmetic Operators

| Operator | Meaning        | Example   | Result |
| -------- | -------------- | --------- | -----: |
| `+`      | Addition       | `10 + 3`  |   `13` |
| `-`      | Subtraction    | `10 - 3`  |    `7` |
| `*`      | Multiplication | `10 * 3`  |   `30` |
| `/`      | Division       | `10 / 4`  |  `2.5` |
| `//`     | Floor division | `10 // 3` |    `3` |
| `%`      | Modulo         | `10 % 3`  |    `1` |
| `**`     | Exponentiation | `2 ** 3`  |    `8` |

Example:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Division `/` returns a division result, commonly a float. Floor division `//` rounds down toward negative infinity.

```python
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(-7 // 2)  # -4
```

Modulo returns the remainder according to Python's division rules. It is useful for divisibility checks.

```python
print(10 % 2)  # 0
print(11 % 2)  # 1
```

Exponentiation raises a value to a power:

```python
print(2 ** 4)  # 16
```

Division by zero raises `ZeroDivisionError`.

## 4. Comparison Operators

Comparison operators compare values and return a Boolean result.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

Example:

```python
age = 22

print(age == 22)
print(age != 18)
print(age > 18)
print(age < 18)
print(age >= 22)
print(age <= 21)
```

`=` assigns a value. `==` compares two values.

Python supports chained comparisons:

```python
age = 22
print(18 <= age <= 60)
```

This is true when the age is within the inclusive range from 18 to 60.

## 5. Logical Operators

Logical operators combine or reverse conditions.

- `and`: true only when both conditions are true.
- `or`: true when at least one condition is true.
- `not`: reverses the truth value.

```python
age = 22
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)
```

Logical operators are useful for eligibility rules, input validation, and combining multiple requirements.

Python's logical operators can short-circuit: `and` may stop after a false operand, and `or` may stop after a true operand. They can return an operand rather than always returning a Boolean, although common comparison-based conditions usually produce Boolean values.

## 6. Assignment Operators

Assignment associates a value with a variable. Augmented assignment operators update a variable using an operation.

```python
score = 10
score += 5
print(score)
```

`score += 5` is equivalent in this case to `score = score + 5`.

Common augmented assignment operators include:

- `+=`
- `-=`
- `*=`
- `/=`
- `//=`
- `%=`
- `**=`

Example:

```python
number = 10
number += 2
number -= 3
number *= 2

print(number)
```

Understand each update in sequence: each operation uses the current value of `number`.

## 7. Operator Precedence

Operator precedence determines the order in which parts of an expression are evaluated.

```python
print(2 + 3 * 4)     # 14
print((2 + 3) * 4)   # 20
print(2 ** 3 ** 2)   # 512
```

Multiplication occurs before addition. Parentheses change the order. Exponentiation groups from right to left.

A simplified precedence guide, from higher to lower:

1. Parentheses and grouping.
2. Exponentiation.
3. Multiplication, division, floor division, modulo.
4. Addition and subtraction.
5. Comparisons.
6. `not`.
7. `and`.
8. `or`.

This is a simplified reference, not the complete Python precedence table. Parentheses can improve clarity even when they are not strictly required.

## 8. Membership Operators

`in` and `not in` test membership.

```python
language = "Python"

print("Py" in language)
print("Java" in language)
print("Java" not in language)
```

For strings, membership checks whether one string is contained in another. Membership also works with collection types.

## 9. Identity Operators

`is` and `is not` test object identity: whether two references point to the same object.

```python
result = None

print(result is None)
print(result is not None)
```

Use `is None` when checking for `None`.

Equality and identity are different:

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True: equal contents
print(a is b)  # False: different list objects
```

Use `==` to compare values in ordinary comparisons; use identity checks where object identity is intended.

## 10. Practical Project: Calculator

```python
first_number = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        result = None
        print("Error: division by zero is not allowed.")
    else:
        result = first_number / second_number
else:
    result = None
    print("Unsupported operator.")

if result is not None:
    print(f"Result: {result}")
```

This project combines input, numeric conversion, comparison, arithmetic, conditional logic, and output formatting.

The program expects numeric input. Invalid numeric text causes a conversion error; robust input validation will be added in a later lesson.

## 11. Connection to AI and Machine Learning

Operators are fundamental to calculations and decision logic in software.

Examples include:

- Calculating totals and averages.
- Comparing scores against thresholds.
- Combining validation rules.
- Checking whether a result is missing.
- Applying mathematical transformations to data.

Machine-learning libraries provide additional numerical operations, but Python operators remain important for application logic, data preparation, and evaluation code.

## 12. Exercises

### Exercise 1 — Arithmetic Explorer

Create `exercises/exercise-01.py`.

Store two numbers and display their sum, difference, product, division, floor division, remainder, and exponentiation. Test with `17` and `5`.

### Exercise 2 — Comparison and Logic Tester

Create `exercises/exercise-02.py`.

Create variables for age, score, and registration status. Print comparisons and determine whether all requirements are met using `and`. Test both true and false cases.

### Exercise 3 — Shopping Bill Calculator

Create `exercises/exercise-03.py`.

Ask for a price and quantity, calculate a subtotal, and apply a 10% discount when the subtotal is at least 1,000. Display the final amount.

Use appropriate numeric conversions, arithmetic operators, comparisons, and conditional logic.

## 13. Troubleshooting

### `ZeroDivisionError`

Check whether a divisor is zero before dividing.

### `TypeError`

Confirm that the operands support the requested operation. Convert compatible input strings to numbers before arithmetic.

### Unexpected comparison result

Check the difference between `=` and `==`, and verify the actual variable values.

### Unexpected calculation order

Use parentheses to make the intended precedence clear.

### `ValueError`

Check that numeric input is in a format accepted by `int()` or `float()`.

## 14. Learning Resources

- Python tutorial: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- Python expressions and operators: [https://docs.python.org/3/reference/expressions.html](https://docs.python.org/3/reference/expressions.html)
- Python built-in types: [https://docs.python.org/3/library/stdtypes.html](https://docs.python.org/3/library/stdtypes.html)
- Corey Schafer's Python tutorials: [https://www.youtube.com/@Coreyms](https://www.youtube.com/@Coreyms)
- freeCodeCamp programming courses: [https://www.youtube.com/@freecodecamp](https://www.youtube.com/@freecodecamp)

Read relevant sections and run the examples yourself.

## 15. Key Takeaways

- Arithmetic operators calculate values.
- Comparison operators return Boolean results.
- Logical operators combine conditions.
- Assignment operators update variables.
- Precedence controls evaluation order.
- Membership checks whether an item is present.
- Identity checks whether references point to the same object.
- Parentheses improve clarity.
- Operators are fundamental to algorithms and AI/ML application logic.

## 16. Completion Checklist

- [x] Arithmetic operators practiced.
- [x] Comparison operators practiced.
- [x] Logical operators practiced.
- [x] Assignment operators practiced.
- [x] Operator precedence tested.
- [x] Membership and identity understood.
- [x] Calculator program completed and tested.
- [x] All three exercises completed.
- [x] Learning log updated.
- [x] README saved.
- [x] Changes committed and pushed to GitHub.
- [x] LinkedIn post prepared.
- [x] Day 3 assessment passed.