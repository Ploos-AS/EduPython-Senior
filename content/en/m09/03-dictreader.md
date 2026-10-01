# M9.3 — Column Names with `csv.DictReader`

With `csv.reader`, each row became a list:

```python
["January", "820"]
```

That means we have to remember that `row[0]` is the month and `row[1]` is the electricity use. This works, but becomes harder when a file has more columns.

When a CSV file has a header, `csv.DictReader` can use the column names for us.

## From list to dictionary

```python
import csv
from pathlib import Path

path = Path(__file__).with_name("energy.csv")

with open(path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

Run `examples/m09/read_csv_dict.py`.

A data row now contains names and values approximately like this:

```text
{'month': 'January', 'kwh': '820'}
```

This builds directly on the dictionaries you learned about in M7.

## The header gets a job

The file starts with:

```text
month,kwh
```

`DictReader` uses these fields as keys. The header is therefore not returned as an ordinary data row.

For this row:

```text
January,820
```

we can access the fields with:

```python
print(row["month"])
print(row["kwh"])
```

This is often clearer than:

```python
print(row[0])
print(row[1])
```

The column name tells us what the value means.

## Print a clear sentence

The example program uses:

```python
for row in reader:
    print(row["month"], ":", row["kwh"], "kWh")
```

The result is:

```text
January : 820 kWh
February : 760 kWh
March : 640 kWh
April : 510 kWh
```

Notice that `row["kwh"]` is still text. `DictReader` gives us names for the fields, but it does not convert their data types.

## What if the name is wrong?

A dictionary requires the correct key. If you write:

```python
row["energy"]
```

but the header contains only `month` and `kwh`, you get a `KeyError`.

This is the same kind of error you met with dictionaries in M7. Read the error message and compare the key with the header in the CSV file.

## Try it

Run:

```text
python examples/m09/read_csv_dict.py
```

Compare the code with `read_csv.py` from the previous lesson.

## Change it

Change the output so it begins with:

```text
Use in January: 820 kWh
```

You do not need to change the CSV file.

## Make it yourself

Create a CSV file with this header:

```text
title,year
```

Add at least three rows. Read the file with `csv.DictReader` and print `row["title"]` and `row["year"]`.

Finally, try changing the order of the columns in both the header and the data rows. When you use column names, the rest of the program can remain easy to understand.

### Remember

`csv.DictReader` uses the header as keys and turns each data row into a dictionary. The values are still text.
