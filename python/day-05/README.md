# Day 5 — Python Loops: `for` and `while`

## 1. Learning Objectives

- Understand loops and repetitive execution.
- Use `for` and `while` loops.
- Iterate over `range()`, strings, and lists.
- Use accumulators for totals and averages.
- Understand `break` and `continue`.
- Write nested loops.
- Avoid infinite loops and off-by-one errors.
- Build practical programs and complete coding exercises.

## 2. What Is a Loop?

A loop repeats a block of code. Loops reduce repetitive code and are useful for processing collections, performing calculations, and automating tasks.

Python provides `for` and `while` loops.

## 3. The `for` Loop

A `for` loop iterates over items in an iterable.

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

`range(start, stop)` includes the starting value but excludes the stopping value.

`range(start, stop, step)` also specifies the increment.

```python
for number in range(2, 11, 2):
    print(number)
```

A `for` loop can also iterate over strings and lists.

```python
for character in "Python":
    print(character)
```

## 4. Accumulators

An accumulator stores a running result.

```python
total = 0

for number in range(1, 6):
    total += number

print(total)
```

Output: `15`.

The accumulator must be initialized before the loop and updated during each iteration.

## 5. The `while` Loop

A `while` loop repeats as long as its condition is true.

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

The variable changes during each iteration. Without an appropriate update, the loop may never end.

## 6. `break` and `continue`

- `break` exits the loop immediately.
- `continue` skips the remainder of the current iteration and moves to the next one.

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

This prints 1, 2, 4, and 5.

## 7. Nested Loops

A nested loop places one loop inside another.

```python
for row in range(1, 4):
    for column in range(1, 3):
        print(row, column)
```

The inner loop completes its iterations for each outer-loop iteration.

## 8. Practical Projects

### Multiplication Table

Create `multiplication-table.py`. Ask for an integer and display its multiplication table from 1 through 10.

### Number Guessing Game

Create `number-guessing-game.py`. Use a `while` loop to repeat guesses until the user guesses a fixed secret number. Count attempts and provide higher-or-lower feedback.

## 9. Exercises

1. **Number sequence:** print numbers 1–50, print the even numbers, and calculate the sum.
2. **Factorial calculator:** calculate the factorial of a non-negative integer using a loop. Remember that 0 factorial is 1.
3. **Input until zero:** repeatedly accept numbers until zero is entered; display the count and sum of the non-zero inputs.
4. **Pattern printer:** use nested loops to print a five-row star pattern and then try printing it upside down.

Test ordinary inputs and boundary cases.

## 10. Common Errors

- Infinite loops caused by conditions that never become false.
- Off-by-one errors caused by misunderstanding `range()`.
- Incorrect indentation.
- Accumulators initialized or updated in the wrong place.
- Incorrect use of `break` and `continue`.
- Conversion errors when non-numeric text is entered.

## 11. Connection to AI/ML

Loops can process records, calculate statistics, inspect predictions, automate repetitive tasks, and help explain iterative algorithms. Libraries such as NumPy and Pandas also offer optimized operations for processing numerical arrays and tables.

## 12. Learning Resources

- Python Tutorial: [https://docs.python.org/3/tutorial/controlflow.html](https://docs.python.org/3/tutorial/controlflow.html)
- Python compound statements: [https://docs.python.org/3/reference/compound_stmts.html](https://docs.python.org/3/reference/compound_stmts.html)
- Corey Schafer: [https://www.youtube.com/@Coreyms](https://www.youtube.com/@Coreyms)
- freeCodeCamp: [https://www.youtube.com/@freecodecamp](https://www.youtube.com/@freecodecamp)

## 13. Completion Checklist

- [x] Understand `for` loops.
- [x] Practise `range()` and its stop boundary.
- [x] Iterate over strings and lists.
- [x] Calculate totals using an accumulator.
- [x] Understand `while` loops.
- [x] Practise `break` and `continue`.
- [x] Understand nested loops.
- [x] Complete both practical projects.
- [x] Complete all four exercises.
- [x] Test boundary cases.
- [x] Update the learning log.
- [x] Save and review this README.
- [x] Commit and push the Day 5 files.
- [x] Complete the Day 5 assessment.