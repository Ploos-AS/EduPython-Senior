# M9.4 — Numbers and Calculations from CSV

In M9.3 we could access the electricity use with:

```python
row["kwh"]
```

But the value is still text. For example, `"820"` is a string. If we want to add and calculate with the values, we must first turn them into numbers.

## From text to integer

We already know `int()`:

```python
kwh = int(row["kwh"])
```

Now `kwh` is the number `820`, not the text `"820"`.

This is an important rule when working with CSV:

> Read the data as text first. Convert only the fields you know should be numbers.

## Collect the numbers

We can read all measurements into a list:

```python
values = []

for row in reader:
    kwh = int(row["kwh"])
    values.append(kwh)
```

Afterwards, the list contains:

```python
[820, 760, 640, 510]
```

Python can now calculate with the values.

## Count and total

```python
count = len(values)
total = sum(values)
```

For the example data we get:

```text
Count: 4
Total: 2730 kWh
```

You already know `len()` from lists. `sum()` adds the numbers in the list.

## Minimum and maximum

Python also provides:

```python
lowest = min(values)
highest = max(values)
```

These find the lowest and highest values in the list.

## Average

The average is the total divided by the count:

```python
average = total / count
```

With our dataset, the result is:

```text
Average: 682.5 kWh
```

This is ordinary division from earlier in the course. We are not using advanced statistics.

## The complete program

Run `examples/m09/energy_summary.py`.

The program:

1. opens the CSV file
2. uses `DictReader`
3. converts `kwh` to `int`
4. stores the numbers in a list
5. calculates count, total, minimum, maximum, and average

This combines knowledge from several earlier milestones.

## One important assumption

`min()`, `max()`, and the division used for the average need at least one value.

Our example file contains data, so the program can use them directly. In later programs we will also consider empty and incomplete datasets.

## Try it

Run:

```text
python examples/m09/energy_summary.py
```

Check that you get:

```text
Count: 4
Total: 2730 kWh
Minimum: 510 kWh
Maximum: 820 kWh
Average: 682.5 kWh
```

## Change it

Add:

```text
May,430
```

to `energy.csv`.

Before running the program, try calculating the new total yourself. Then run it and compare.

## Make it yourself

Create a CSV file with one text column and one numeric column, for example:

```text
place,temperature
Grimstad,18
Tonstad,14
Kristiansand,17
```

Read the numeric column, convert it with `int()`, and find the total, minimum, maximum, and average.

### Remember

CSV values start as text. When you know a field represents an integer, convert it explicitly with `int()` and then use ordinary Python calculations.
