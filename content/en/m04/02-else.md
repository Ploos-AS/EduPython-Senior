# M4.2 – Two possible paths with else

An `if` can decide whether a block of code should run. Often, we instead want the program to choose between **two** paths.

For that, we use `else`.

## Try it

```python
temperature = float(input("Temperature: "))

if temperature < 0:
    print("The temperature is below zero.")
else:
    print("The temperature is zero or above.")
```

The program runs exactly one of the two messages.

If the condition is true, the block under `if` runs.

If the condition is false, the block under `else` runs.

## else has no condition of its own

Notice:

```python
else:
```

We do not write another question after `else`.

`else` simply means: **otherwise** – when the `if` condition was not true.

## Boundary values matter

In the example, the condition is:

```python
temperature < 0
```

What happens when the temperature is exactly `0`?

The expression `0 < 0` is false, so the program takes the `else` path.

When writing conditions, always think about the boundary itself.

## Change it

Try:

```python
number = int(input("Enter an integer: "))

if number >= 10:
    print("The number is at least 10.")
else:
    print("The number is less than 10.")
```

Run the program with:

- `9`
- `10`
- `11`

Pay particular attention to what happens with `10`.

## Indentation shows the two blocks

```python
if number >= 10:
    print("First path")
    print("The condition was true.")
else:
    print("Second path")
    print("The condition was false.")

print("This line runs after the decision.")
```

After one of the blocks finishes, the program continues with code that is no longer indented under `if` or `else`.

## A common structural error

This is wrong:

```python
if number >= 10:
    print("At least 10")
    else:
        print("Less than 10")
```

`else` belongs at the same indentation level as `if`:

```python
if number >= 10:
    print("At least 10")
else:
    print("Less than 10")
```

When Python complains about the structure around `else`, check the colons and indentation first.

## Make it yourself

Create a program that:

- asks for one value
- converts it to a number
- uses `if` and `else`
- prints one message when the condition is true
- prints another when it is false

Test values on both sides of the boundary, and test the boundary value itself.

## What you learned

You can now:

- use `if` and `else` together
- explain that only one of the two blocks runs
- explain what `else` means
- investigate what happens at a boundary value
- place `if` and `else` at the correct indentation level

The next lesson introduces `elif` when a program needs more than two possible paths.
