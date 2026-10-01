# M9.8 — Practical Project: Electricity Report

Now we will combine the most important parts of M9 in one program.

The program will:

1. read a CSV file
2. use column names
3. check missing and invalid values
4. convert valid numbers
5. store structured data
6. calculate a summary
7. filter using a limit

This is not a new technique. It is practice in combining things you already know.

## The dataset

`examples/m09/energy_report.csv` contains both valid and invalid rows.

Some values are missing or cannot be converted to integers. The program should report those rows and continue with the valid ones.

## Divide the work with functions

We create one function for reading and validation:

```python
def read_measurements(path):
```

It returns a list of dictionaries where `kwh` is already an integer.

The rest of the program therefore does not need to ask whether the value is still text or whether it is valid.

## A clear data structure

A valid row is stored like this:

```python
{"month": month, "kwh": kwh}
```

This uses lists and dictionaries from M7.

## The summary

The second function receives the validated measurements:

```python
def print_report(measurements, limit):
```

It calculates:

- number of valid measurements
- total
- minimum
- maximum
- average

It then displays only measurements that are at least as large as `limit`.

## An empty dataset

This time we also handle the case where there are no valid measurements:

```python
if len(measurements) == 0:
    print("No valid measurements")
    return
```

This prevents us from using `min()`, `max()`, or division on an empty collection.

## Run the program

```text
python examples/m09/energy_report.py
```

Study the output in this order:

1. which rows were skipped?
2. how many valid measurements are there?
3. is the total correct?
4. which months pass the 700 kWh limit?

Try to answer before changing the program.

## Change it

Change the limit from:

```python
print_report(measurements, 700)
```

to:

```python
print_report(measurements, 500)
```

Predict which months will now appear in the filtered section.

## Make it yourself — cumulative M9 project

Choose a small dataset that is useful or interesting to you. For example:

- monthly expenses
- temperature measurements
- books and page counts
- travel distances
- time spent on activities

Create at least two columns: one text column and one numeric column.

Your program should:

1. read the CSV file with `DictReader`
2. convert the numeric field explicitly
3. detect empty and invalid numbers
4. store valid rows
5. calculate at least a total and an average
6. filter using a limit you choose
7. print an understandable result

### Extra challenge

Write the validated rows to a new CSV file with `DictWriter`.

Use a new file. Do not overwrite the original data while working on the project.

## Check your work

Before considering the project complete, try at least these cases:

- every row is valid
- one numeric field is empty
- one numeric field contains text
- no rows pass the filter

The program should produce an understandable result without requiring you to edit the Python code between tests, except for the data or the limit you deliberately want to try.

## What you can now do

After M9, you can use Python to work with simple tabular data without installing extra libraries.

You can read, check, convert, summarize, filter, and write CSV. Just as importantly, you can combine files, functions, lists, dictionaries, loops, and decisions in one coherent program.

That is a major step from the first `print()` lines in the course.
