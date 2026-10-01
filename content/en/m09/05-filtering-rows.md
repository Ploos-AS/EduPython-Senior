# M9.5 — Filtering Rows

A dataset often contains more rows than we need right now. We can **filter** it by selecting only the rows that meet a condition.

This builds directly on `if` from M4.

## Select high usage

We want to find months where electricity use is at least 700 kWh.

```python
for row in reader:
    kwh = int(row["kwh"])

    if kwh >= 700:
        print(row["month"], kwh)
```

With `energy.csv`, the result is:

```text
January 820
February 760
```

The program reads every row, but prints only the rows that match the condition.

## Order matters

The CSV value starts as text:

```python
row["kwh"]
```

Before comparing it with the number `700`, we convert it:

```python
kwh = int(row["kwh"])
```

Then this comparison makes sense:

```python
if kwh >= 700:
```

We are comparing numbers with numbers.

## Store the selected rows

We can also collect the results in a list:

```python
selected = []

for row in reader:
    kwh = int(row["kwh"])

    if kwh >= 700:
        selected.append(row)
```

Now `selected` contains only the dictionaries that met the condition.

This combines:

- CSV files
- dictionaries
- loops
- `int()`
- `if`
- lists

## A limit as a variable

It is clearer to give the limit a name:

```python
limit = 700
```

Then:

```python
if kwh >= limit:
```

Now we can change one value when we want to try another limit.

## Try it

Run:

```text
python examples/m09/filter_energy.py
```

The program prints months with at least 700 kWh of electricity use.

## Change it

Change:

```python
limit = 700
```

to:

```python
limit = 600
```

Before running the program, try to work out which months will now be selected.

## Make it yourself

Change the condition so the program instead finds months with **less than 700 kWh**.

Then try two limits:

```python
minimum = 600
maximum = 800
```

You can use what you learned about `and` in M4:

```python
if kwh >= minimum and kwh <= maximum:
```

Which rows are selected?

### Remember

Filtering does not change the CSV file. The program reads the data and chooses which rows it wants to work with.
