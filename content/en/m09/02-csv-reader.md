# M9.2 — Reading CSV with `csv.reader`

In the previous lesson we read the CSV file as ordinary text. Now Python will help us split the file into **rows and fields**.

Python includes the `csv` module in its standard library, so you do not need to install anything extra.

## Your first CSV reader

```python
import csv
from pathlib import Path

path = Path(__file__).with_name("energy.csv")

with open(path, "r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Run `examples/m09/read_csv.py`.

You should see something like:

```text
['month', 'kwh']
['January', '820']
['February', '760']
['March', '640']
['April', '510']
```

## What does `csv.reader` do?

`csv.reader(file)` creates a reader that understands CSV structure.

When the loop asks for the next row, the reader splits that row into fields. Each row becomes a **list**. This connects directly to what you learned about lists in M7.

The first row becomes:

```python
["month", "kwh"]
```

The second row becomes:

```python
["January", "820"]
```

## The header is a row too

`csv.reader` does not automatically know that the first row is a header. To the reader, it is simply the first row in the file.

Later we will meet another CSV reader that can use column names directly. First, it is useful to see the simple structure clearly.

## Everything is still text

Notice this row:

```python
["January", "820"]
```

The value `"820"` has quotation marks when the list is displayed. That means it is a string, not the number `820`.

A CSV file stores text. Python does not guess which fields should be integers, decimal numbers, dates, or something else. We will make those conversions deliberately in a later lesson.

## Why `newline=""`?

When Python's `csv` module works with a file, the recommended pattern is to open it with `newline=""`. This lets the CSV module handle newlines itself.

You do not need all the details yet. Use this pattern when opening CSV files:

```python
with open(path, "r", encoding="utf-8", newline="") as file:
```

## Try it

Run:

```text
python examples/m09/read_csv.py
```

Identify:

1. the header row
2. the January row
3. the two fields in each row

## Change it

Add:

```text
May,430
```

to `energy.csv` and run the program again.

Then try changing the output to:

```python
for row in reader:
    print("Number of fields:", len(row), row)
```

Every row in this dataset should contain two fields.

## Make it yourself

Create a small CSV file with three columns. Read it with `csv.reader` and print each row.

Then try printing only the first field:

```python
for row in reader:
    print(row[0])
```

You are now combining files, loops, lists, and indexing from earlier milestones.

### Remember

`csv.reader` turns each CSV row into a list of text values. This makes CSV data available through Python tools you already know.
