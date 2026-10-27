# Day 6 — Python Loop Practice and Problem-Solving

## Learning Objectives

- Strengthen `for` and `while` loop skills.
- Use counters and accumulators.
- Solve problems with loops, conditions, and arithmetic.
- Calculate sums, averages, and factorials.
- Implement a basic prime number checker.
- Practise nested loops and number patterns.
- Build a menu-driven calculator.
- Test boundary cases and explain code logic.

## Topics Covered

### 1. Counters and Accumulators

A counter tracks occurrences. An accumulator stores a running result.

```python
count = 0
total = 0

for number in range(1, 6):
    count += 1
    total += number

print("Count:", count)
print("Total:", total)
```

### 2. Sum and Average

Use a loop to calculate the sum of numbers from 1 through `n`. Calculate the average by dividing the sum by `n`. Validate that `n` is positive before division.

### 3. Factorial

Factorial multiplies the positive integers up to `n`. By definition, `0! = 1`.

### 4. Prime Numbers

A prime number is an integer greater than 1 with exactly two positive divisors. The beginner implementation checks divisors from 2 to `n - 1` and stops when it finds a divisor.

### 5. Nested Loops

Nested loops are useful for generating number patterns, star patterns, and combinations of rows and columns.

### 6. Menu-Driven Programs

Use a `while` loop to repeat a menu, conditionals to handle each choice, and `break` to exit.

## Practical Programs

- `loop-revision.py`
- `sum-and-average.py`
- `factorial.py`
- `prime-checker.py`
- `number-patterns.py`
- `menu-driven-calculator.py`

## Exercises

1. Count even and odd numbers and calculate their separate sums.
2. Reverse the digits of a non-negative integer using a `while` loop.
3. Build a guessing game with a maximum of five attempts.
4. Calculate the total, average, highest mark, and lowest mark for student scores.
5. Print numbers divisible by 3 and 5, then implement FizzBuzz.

Store exercises in the `exercises/` directory.

## Testing Strategy

Test typical inputs and boundary cases. Include zero, negative numbers, minimum valid values, and conditions such as division by zero. For programs that accept user input, consider what happens when input is invalid.

## Connection to AI/ML

Counters, accumulators, loops, and conditions are foundational programming techniques for data processing, statistics, validation, and algorithm implementation. Later, Python libraries such as NumPy and Pandas will help process numerical arrays and tables efficiently.

## Learning Resources

- Python control flow tutorial: [https://docs.python.org/3/tutorial/controlflow.html](https://docs.python.org/3/tutorial/controlflow.html)
- Python compound statements: [https://docs.python.org/3/reference/compound_stmts.html](https://docs.python.org/3/reference/compound_stmts.html)
- Corey Schafer: [https://www.youtube.com/@Coreyms](https://www.youtube.com/@Coreyms)
- freeCodeCamp: [https://www.youtube.com/@freecodecamp](https://www.youtube.com/@freecodecamp)

## Completion Checklist

- [x] Review `for` and `while` loops.
- [x] Complete the sum and average program.
- [x] Complete the factorial program.
- [x] Complete the prime checker.
- [x] Complete number patterns.
- [x] Complete the menu-driven calculator.
- [x] Solve all five exercises.
- [x] Test boundary cases.
- [x] Update the learning log.
- [x] Review the code and README.
- [x] Commit and push changes to GitHub.
- [x] Pass the Day 6 assessment.