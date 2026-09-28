# M4.5 – A practical decision program

Now we combine what you have learned about input, numbers, and decisions.

We will build a program that describes a temperature.

## Try it

```python
temperature = float(input("Temperature: "))

if temperature < 0:
    message = "Below zero"
elif temperature >= 0 and temperature < 10:
    message = "Cool"
elif temperature >= 10 and temperature < 20:
    message = "Mild"
else:
    message = "20 or above"

print("Assessment:")
print(message)
```

The program:

1. reads data
2. converts the text to a number
3. tests conditions
4. chooses one message
5. prints the result

Notice that the branches store a value in `message`. The actual output happens only once after the decision.

## Follow one value through the program

Suppose the user enters `12`.

Python tests:

```python
temperature < 0
```

False.

Then:

```python
temperature >= 0 and temperature < 10
```

False.

Then:

```python
temperature >= 10 and temperature < 20
```

True.

So:

```python
message = "Mild"
```

The remaining branches are skipped.

## Test the boundaries

A decision program should not be tested only with random numbers.

Try:

- `-1`
- `0`
- `9.9`
- `10`
- `19.9`
- `20`

For each value, first decide which message you expect, then run the program.

This is a simple form of systematic testing.

## Can the conditions be simplified?

Because earlier branches have already excluded lower values, some conditions could be written more briefly.

However, the explicit form:

```python
temperature >= 10 and temperature < 20
```

shows the range clearly while we are learning.

Readable code matters more than making every line as short as possible.

## Change it

Create your own boundaries and messages.

Write down the boundaries before changing the code. Then test:

- just below each boundary
- exactly at each boundary
- just above each boundary

## Make it yourself

Build a decision program for another subject.

Requirements:

- at least one value from `input()`
- any required conversion
- `if`
- at least one `elif`
- `else`
- at least one comparison
- at least one clear result variable
- boundary-value tests

Possible themes include time spent, energy use, distance, scores, or another numeric range of your choice.

## What you learned

You can now combine:

**data in → conversion → decision → result**

You can also test a decision program systematically around its boundaries.

The next section practises all of M4 with exercises and debugging.
