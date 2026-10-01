# M9.6 — Missing and Invalid Data

Real data is not always perfect. A field may be empty, or it may contain text where the program expects a number.

That does not mean we should ignore errors. We should **detect them, understand them, and handle the errors we expect**.

## A controlled example

The file `examples/m09/energy_with_errors.csv` contains:

```text
month,kwh
January,820
February,
March,unknown
April,510
```

There are two different problems:

- February has a missing value
- March contains the text `unknown` where we expect an integer

These cases should be handled clearly.

## Check for an empty value first

We get the text and remove surrounding whitespace:

```python
text = row["kwh"].strip()
```

Then we can test:

```python
if text == "":
    print(month, ": missing value")
    continue
```

`continue` moves to the next loop iteration. We therefore do not try to convert an empty string with `int()`.

## When the text is not a number

A non-empty value can still be invalid:

```text
unknown
```

This code raises `ValueError`:

```python
int("unknown")
```

Here we know exactly which error can occur, so we can handle specifically `ValueError`:

```python
try:
    kwh = int(text)
except ValueError:
    print(month, ": invalid number:", text)
    continue
```

We do not use a general `except:`. Other errors should remain visible so that we can find and fix them.

## Keep the valid values

When conversion succeeds:

```python
valid_values.append(kwh)
```

The program can continue with valid data while still reporting which rows had problems.

Run `examples/m09/read_imperfect_csv.py`.

You should see January and April accepted, while February and March receive clear messages.

## Why not just ignore everything that goes wrong?

If we hide every error, a program can produce a result that looks correct even when important data is missing.

A better pattern is:

1. check for expected missing values
2. handle the specific conversion error
3. make the problem visible
4. keep only values you have actually validated

## Try it

Run:

```text
python examples/m09/read_imperfect_csv.py
```

Find the two different error cases in the output.

## Change it

Change `unknown` to `640` and run the program again.

How many valid values do you get now?

Then give February the value `760`. All four rows should now be valid.

## Make it yourself

Create a CSV file containing names and ages. Leave one age empty and make another contain text that is not a number.

Write a program that:

- reports an empty age
- catches only `ValueError` for an invalid number
- prints valid ages
- counts how many valid values it found

### Remember

Robust code does not mean hiding errors. It handles expected problems clearly and leaves unexpected errors visible.
