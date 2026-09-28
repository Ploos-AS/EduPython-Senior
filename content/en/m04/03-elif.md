# M4.3 – More paths with elif

With `if` and `else`, a program can choose between two paths. Sometimes we need more.

For that, we use `elif`, which can be read as **else if**.

## Try it

```python
temperature = float(input("Temperature: "))

if temperature < 0:
    print("Below zero.")
elif temperature < 20:
    print("From 0 to below 20.")
else:
    print("20 or above.")
```

The program chooses one of three paths.

## Python tests from top to bottom

Python does this:

1. tests `temperature < 0`
2. if it is true, that block runs and the rest is skipped
3. otherwise, `temperature < 20` is tested
4. if that is also false, the `else` block runs

Only the **first true branch** runs.

## Why does order matter?

Look at:

```python
if temperature < 20:
    print("Below 20")
elif temperature < 0:
    print("Below zero")
```

If the temperature is `-5`, `temperature < 20` is already true. Python runs the first block and never reaches the `temperature < 0` test.

When conditions overlap, they therefore need a sensible order.

## Boundaries again

In the first program:

- `-1` takes the first branch
- `0` takes the `elif` branch
- `19.9` takes the `elif` branch
- `20` takes the `else` branch

Try those exact values.

## More than one elif

You can have several `elif` branches:

```python
score = int(input("Score: "))

if score < 25:
    print("Level 1")
elif score < 50:
    print("Level 2")
elif score < 75:
    print("Level 3")
else:
    print("Level 4")
```

Again, the branches are tested from top to bottom.

## else is still optional

A chain does not always need `else`:

```python
number = int(input("Number: "))

if number < 0:
    print("Negative")
elif number == 0:
    print("Zero")
```

If the number is positive, this code prints nothing.

Use `else` when you actually need a final path for all remaining cases.

## Change it

Create three temperature categories with different boundaries. Test:

- a value below the first boundary
- exactly the first boundary
- a value between the boundaries
- exactly the second boundary
- a value above the second boundary

## A common reasoning error

Do not ask only, “Is each condition correct?” Also ask:

**Could an earlier condition already have caught this value?**

That is an important part of debugging `if`/`elif` logic.

## Make it yourself

Create a program with at least three possible outcomes.

The program should:

- read one value with `input()`
- convert the value
- use `if`, at least one `elif`, and `else`
- print different messages for the different ranges
- be tested at the boundaries between ranges

## What you learned

You can now:

- use `elif`
- create more than two possible paths
- explain that Python tests from top to bottom
- explain that the first true branch wins
- order overlapping conditions sensibly
- test boundary values systematically

The next lesson combines simple conditions with `and`, `or`, and `not`.
