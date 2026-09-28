# M4.6 – Exercises and debugging

These exercises bring all of M4 together. Try each one before reading the guidance.

## 1. True or false?

Assume:

```python
number = 10
```

What are the results of:

```python
number > 5
number == 10
number != 10
number <= 9
```

**Answers:**

- `number > 5` → true
- `number == 10` → true
- `number != 10` → false
- `number <= 9` → false

## 2. = or ==?

Which line stores a value?

```python
age = 70
age == 70
```

**Answer:** `age = 70` stores the value. `age == 70` compares.

## 3. Find the syntax error

```python
temperature = float(input("Temperature: "))

if temperature < 0
    print("Below zero")
```

**Answer:** The condition is missing a colon:

```python
if temperature < 0:
```

## 4. Find the indentation error

```python
number = int(input("Number: "))

if number >= 10:
print("At least 10")
else:
    print("Below 10")
```

The line under `if` must be indented:

```python
if number >= 10:
    print("At least 10")
else:
    print("Below 10")
```

## 5. What happens at the boundary?

```python
if temperature < 20:
    print("Below 20")
else:
    print("20 or above")
```

What is printed when `temperature` is exactly `20`?

**Answer:** `20 or above`, because `20 < 20` is false.

## 6. Find the logic error

```python
if temperature < 20:
    print("Below 20")
elif temperature < 0:
    print("Below zero")
else:
    print("20 or above")
```

Why will `-5` never produce `Below zero`?

**Answer:** The first condition, `temperature < 20`, is already true for `-5`. The first true branch wins.

One possible correction:

```python
if temperature < 0:
    print("Below zero")
elif temperature < 20:
    print("From 0 to below 20")
else:
    print("20 or above")
```

## 7. Complete the range

Complete the condition so the message is printed only for numbers from 10 through 20:

```python
if number >= 10 __________ number <= 20:
    print("In range")
```

**Answer:**

```python
if number >= 10 and number <= 20:
```

## 8. and or or?

You want to print a message when the temperature is below 0 **or** above 30.

**Possible solution:**

```python
if temperature < 0 or temperature > 30:
    print("Outside the range")
```

## 9. Predict before running

```python
score = 50

if score < 25:
    message = "A"
elif score < 50:
    message = "B"
elif score < 75:
    message = "C"
else:
    message = "D"

print(message)
```

What is printed?

**Answer:** `C`. The condition `score < 50` is false when the score is exactly 50.

## 10. Mini-project

Build an interactive decision program.

Requirements:

- at least one `input()`
- any required `int()` or `float()`
- `if`, `elif`, and `else`
- at least three possible results
- at least one clear comparison
- use `and`, `or`, or `not` where it genuinely makes the program clearer
- store the selected result in a variable
- print the result after the decision
- test just below, at, and just above important boundaries

Consider writing down the expected result before each test.

## Before moving on

You should now be able to explain:

- what a true-or-false condition is
- the difference between `=` and `==`
- why colons and indentation matter
- how `if`, `elif`, and `else` select a branch
- why condition order can change the result
- how `and`, `or`, and `not` are used
- how to test boundary values

The next milestone is about repetition: making a program execute code several times without copying it.
