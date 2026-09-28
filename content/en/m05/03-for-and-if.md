# M5.3 – Decisions inside a loop

A loop can do more than print each value. It can also make a decision for each value.

That means the knowledge from M4 can be used inside a `for` loop.

## Try it

```python
for number in range(1, 6):
    if number < 3:
        print(number, "is less than 3")
    else:
        print(number, "is 3 or greater")
```

The loop visits the numbers 1 through 5.

For each number, Python tests:

```python
number < 3
```

The decision is therefore made again on every iteration.

## Follow the program step by step

When `number` is `1`:

- `1 < 3` is true
- the first message is printed

When `number` is `2`:

- `2 < 3` is true
- the first message is printed

When `number` is `3`:

- `3 < 3` is false
- the `else` message is printed

The same happens for `4` and `5`.

## Two levels of indentation

Look closely at:

```python
for number in range(1, 6):
    if number < 3:
        print("Low number")
```

There are two blocks:

1. the `if` is inside the `for` block
2. the `print()` is inside the `if` block

Indentation shows the structure.

You do not need to count spaces by hand. A normal code editor helps with indentation.

## A decision does not always need else

```python
for number in range(1, 6):
    if number == 3:
        print("Found 3")

    print("Processing", number)
```

The `Found 3` message is printed only once.

`Processing` is printed on every iteration because it is still inside the `for` loop, but not inside the `if`.

## Combined conditions work too

```python
for number in range(1, 11):
    if number >= 4 and number <= 6:
        print(number, "is in the range")
```

Here the `if` test runs for every number from 1 through 10.

## A common indentation mistake

Compare:

```python
for number in range(1, 4):
    if number == 2:
        print("Found 2")
    print("Round", number)
```

with:

```python
for number in range(1, 4):
    if number == 2:
        print("Found 2")

print("Round", number)
```

In the second version, the final `print()` is outside the loop. It runs only once afterwards.

Code can therefore be valid Python and still do something different from what you intended. Indentation is both syntax and program structure.

## Change it

Change the boundary in:

```python
if number < 3:
```

Predict which iterations will take each branch before running the program.

## Make it yourself

Create a program that:

- uses `for` and `range()`
- visits at least five numbers
- uses `if` inside the loop
- produces at least two different kinds of result
- has a message after the entire loop has finished

Predict the result before running the program.

## What you learned

You can now:

- use `if` inside a `for` loop
- explain that the decision is made again on each iteration
- read code with two levels of indentation
- distinguish code inside the `if`, inside the `for`, and after the loop
- spot logical errors caused by incorrect block structure

The next lesson shows how a loop can build up a result over several iterations.
