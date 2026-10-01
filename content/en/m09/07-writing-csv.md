# M9.7 — Writing CSV

So far we have read CSV files. Now we will create a CSV file from Python.

We use `csv.DictWriter` because we are already working with column names and dictionaries.

## Our data

We start with a list of dictionaries:

```python
measurements = [
    {"month": "January", "kwh": 820},
    {"month": "February", "kwh": 760},
    {"month": "March", "kwh": 640},
]
```

Each dictionary will become one data row.

## Tell Python which columns to write

```python
fieldnames = ["month", "kwh"]
```

The order here determines the column order in the CSV file.

## Open the file for writing

```python
with open(path, "w", encoding="utf-8", newline="") as file:
```

As in M8, `"w"` means that the file is created or overwritten.

Always check which path you are using before writing to a real file.

The course example writes only to its own controlled file and removes it afterwards.

## Create the writer

```python
writer = csv.DictWriter(file, fieldnames=fieldnames)
```

Then write the header:

```python
writer.writeheader()
```

and the data rows:

```python
writer.writerows(measurements)
```

The result is:

```text
month,kwh
January,820
February,760
March,640
```

## Read back what you wrote

A useful pattern is to verify the result after writing.

The example program therefore opens the file again with `DictReader` and prints the rows.

We can see the whole path:

```text
Python data → CSV file → Python data
```

## What about `csv.writer`?

Python also has `csv.writer`, which writes sequences such as lists:

```python
writer = csv.writer(file)
writer.writerow(["month", "kwh"])
writer.writerow(["January", 820])
```

This is useful when the data naturally consists of lists. In this course we mainly use `DictWriter` for files with named columns because the names make the code easier to read.

## Try it

Run:

```text
python examples/m09/write_csv.py
```

The program writes a controlled CSV file, reads it back, displays the contents, and removes the file again.

## Change it

Add:

```python
{"month": "April", "kwh": 510}
```

to the list.

Run the program again and check that the new row is read back.

## Make it yourself

Create a list containing at least three dictionaries with these fields:

```text
title,year
```

Write them to a CSV file with `DictWriter`.

Remember:

1. choose the `fieldnames`
2. use `newline=""`
3. write the header
4. write the rows
5. consider reading the file back to verify the result

### Remember

`DictReader` reads named CSV rows into dictionaries. `DictWriter` goes the other way and writes dictionaries as named CSV rows.
