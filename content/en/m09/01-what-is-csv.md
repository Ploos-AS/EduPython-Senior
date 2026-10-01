# M9.1 — What Is CSV?

In M8 you learned to read and write text files. Now we will use text files for **tabular data**.

CSV is a simple way to store rows and columns. The name comes from *Comma-Separated Values*.

A small dataset can look like this:

```text
month,kwh
January,820
February,760
March,640
```

The first row is the **header**. It tells us what the columns mean. The following rows contain data.

Each row here has two fields:

- `month` — the name of the month
- `kwh` — an electricity-use value

## CSV is still text

A CSV file is not a special spreadsheet format. It is an ordinary text file with an agreed structure. You can open it in a text editor and inspect the contents yourself.

Spreadsheet programs can also open CSV files, but we do not need a spreadsheet to work with them in Python.

## The delimiter

A comma is common, but CSV files can use other delimiters, such as semicolons. It is therefore important to know how the file you are working with is actually structured.

We start with commas in this course so the structure is easy to see.

## Try it

The example file `examples/m09/energy.csv` contains:

```text
month,kwh
January,820
February,760
March,640
April,510
```

Our first program still reads the file as ordinary text:

```python
from pathlib import Path

path = Path(__file__).with_name("energy.csv")

with open(path, "r", encoding="utf-8") as file:
    print(file.read())
```

Run `examples/m09/show_csv.py`.

The point is to see that CSV builds directly on what you already know about files. In the next lesson we will use Python's `csv` module to understand the rows and columns.

## Change it

Open `energy.csv` and add another row:

```text
May,430
```

Run the program again. The new row should appear.

## Make it yourself

Create a small CSV file with three columns for something you would like to record. Examples could be date, temperature, and place — or title, author, and year.

You do not need to write Python code that interprets the file yet. The goal is to recognize:

1. the header
2. the rows
3. the columns
4. the delimiter

### Remember

CSV is structured plain text. Before analysing data with Python, we first understand the file format itself.
