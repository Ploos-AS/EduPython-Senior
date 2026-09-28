# M5.4 – Build up a result in a loop

A loop can do more than process each value. It can also build a result little by little.

A common example is adding several numbers.

## Try it

```python
total = 0

for number in range(1, 6):
    total = total + number
    print("After", number, "the total is", total)

print("Final result:", total)
```

The program adds the numbers 1 through 5.

## Three parts

The pattern has three important parts.

### 1. Starting value

```python
total = 0
```

Before the loop begins, we need somewhere to store the result.

### 2. Update

```python
total = total + number
```

You can read this line as:

**Take the old total, add the current number, and store the new total.**

### 3. Final result

```python
print("Final result:", total)
```

This line is after the loop and runs once.

## Follow the value

Start:

```text
total = 0
```

First iteration, `number = 1`:

```text
total = 0 + 1 = 1
```

Second iteration, `number = 2`:

```text
total = 1 + 2 = 3
```

Third iteration, `number = 3`:

```text
total = 3 + 3 = 6
```

The value in `total` therefore carries forward to the next iteration.

## Why must total be before the loop?

This is wrong if the goal is to accumulate the result:

```python
for number in range(1, 6):
    total = 0
    total = total + number
```

Here, `total` is reset to 0 on every iteration. Earlier work is lost.

The starting value must therefore be before the loop:

```python
total = 0

for number in range(1, 6):
    total = total + number
```

## Count events

The same pattern can be used for counting:

```python
count = 0

for number in range(1, 11):
    if number >= 7:
        count = count + 1

print("Count:", count)
```

Here, `count` increases only when the condition is true.

## A shorter notation comes later

Python can write some updates more briefly. For now, we use:

```python
total = total + number
```

because it clearly shows that the old value is used to create the new one.

## Change it

Change:

```python
range(1, 6)
```

to a different range.

Predict the final result before running the program.

## Make it yourself

Create a program that:

- initializes a variable before the loop
- uses a `for` loop
- updates the variable on every iteration or when a condition is true
- prints the final result after the loop

You can add numbers or count how many values satisfy a condition.

## What you learned

You can now:

- initialize a result before a loop
- update the result on each iteration
- explain why the starting value must not be reset inside the loop
- add values
- count events
- distinguish intermediate results from the final result

The next lesson introduces `while`: a loop that continues while a condition is true.
