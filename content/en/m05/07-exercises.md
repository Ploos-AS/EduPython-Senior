# M5.7 – Exercises and debugging

These exercises bring all of M5 together. Try to predict the result before running code.

## 1. How many iterations?

```python
for number in range(4):
    print(number)
```

How many times does `print()` run, and which numbers are printed?

**Answer:** Four times: `0`, `1`, `2`, `3`.

The stopping value `4` is not included.

## 2. Start and stop

What does this print?

```python
for number in range(2, 6):
    print(number)
```

**Answer:**

```text
2
3
4
5
```

## 3. Find the indentation error

```python
for number in range(1, 4):
print(number)
```

**Answer:** The loop needs an indented block:

```python
for number in range(1, 4):
    print(number)
```

## 4. Inside or after the loop?

```python
for number in range(1, 4):
    print("Round", number)

print("Finished")
```

How many times is `Finished` printed?

**Answer:** Once. The line is not indented, so it is after the loop.

## 5. A decision on each iteration

```python
for number in range(1, 5):
    if number >= 3:
        print(number)
```

What is printed?

**Answer:** `3` and `4`.

The condition is tested again for every value.

## 6. Why is the total wrong?

```python
for number in range(1, 4):
    total = 0
    total = total + number

print(total)
```

**Answer:** `total` is reset on every iteration. After the final iteration, it is therefore only `3`.

Move the starting value before the loop:

```python
total = 0

for number in range(1, 4):
    total = total + number

print(total)
```

The result is now `6`.

## 7. Count events

What is the value of `count`?

```python
count = 0

for number in range(1, 8):
    if number > 4:
        count = count + 1

print(count)
```

**Answer:** `3`, because 5, 6, and 7 are greater than 4.

## 8. Trace a while loop

```python
number = 2

while number <= 6:
    print(number)
    number = number + 2
```

What is printed?

**Answer:** `2`, `4`, `6`.

After that, `number` becomes 8 and the condition becomes false.

## 9. Find the infinite loop

```python
number = 1

while number < 5:
    print(number)
```

Why does it not stop?

**Answer:** Nothing changes `number`. The condition `1 < 5` remains true.

One possible correction:

```python
number = 1

while number < 5:
    print(number)
    number = number + 1
```

## 10. for or while?

Choose the simplest loop type.

A. Print the numbers 1 through 10.

B. Keep asking for input while the user enters `yes`.

**Answer:** A `for` loop is a natural fit for A. A `while` loop is a natural fit for B.

## 11. Mini-project

Create a program that processes several measurements.

Requirements:

- use a `for` or `while` loop
- use at least one value that changes during the program
- use a decision inside the loop
- build a total or counter
- print the final result after the loop
- predict at least one test result before running the program

If you use `while`, you should also be able to explain exactly why the loop stops.

## Before moving on

You should now be able to explain:

- what a loop is
- how `for` visits values
- how `range()` determines a number sequence
- that the stopping value in `range()` is not included
- how a decision can be placed inside a loop
- how a result can be built across several iterations
- the difference between code before, inside, and after a loop
- how `while` is controlled by a condition
- why a `while` loop can become infinite
- when a simple `for` or `while` loop is a natural choice

The next milestone is about functions: giving a group of instructions a name so it can be used in an organised way.
