# M5.2 – Repeat a specific number of times with range()

In the previous lesson, `for` visited values we had already written down.

Sometimes we simply want to repeat something a specific number of times. That is where `range()` is useful.

## Try it

```python
for number in range(5):
    print(number)
```

The program prints:

```text
0
1
2
3
4
```

`range(5)` gives the loop five numbers: from `0` through `4`.

## Why does it stop at 4?

In:

```python
range(5)
```

`5` is the **stopping point**, but the stopping point itself is not included.

That means:

- start at 0
- continue while the number is less than 5
- the result is 0, 1, 2, 3, 4

This may feel unfamiliar. Test small values and observe the pattern.

## Repeat five times without using the number

```python
for number in range(5):
    print("This happens five times")
```

The variable `number` still receives the values 0 through 4, even though we do not use it inside the block.

Later, you will encounter a common notation for loops where the value itself is unused. For now, we keep a clear variable name.

## Choose start and stop

`range()` can also receive two numbers:

```python
for number in range(1, 6):
    print(number)
```

This prints:

```text
1
2
3
4
5
```

Read:

```python
range(1, 6)
```

as:

**start at 1, stop before 6.**

## Predict before running

What does this print?

```python
for number in range(3, 7):
    print(number)
```

Predict first.

The answer is:

```text
3
4
5
6
```

## Use the number in a calculation

```python
for number in range(1, 6):
    doubled = number * 2
    print(number, doubled)
```

Each iteration uses the current value of `number`.

## A common reasoning mistake

If you want to print the numbers 1 through 10, this:

```python
range(1, 10)
```

is not enough. It stops before 10.

Use:

```python
range(1, 11)
```

## Change it

Start with:

```python
for number in range(1, 4):
    print("Round", number)
```

Change the stopping value. Predict how many lines will appear before running the program.

## Make it yourself

Create a program that:

- uses `for` and `range()`
- starts at 1
- runs at least five iterations
- uses the loop variable in a calculation
- prints the result in each iteration

## What you learned

You can now:

- use `range(stop)`
- explain that `range()` stops **before** the stopping value
- use `range(start, stop)`
- predict which numbers a simple `range()` produces
- use the loop variable in calculations

The next lesson combines loops with decisions.
