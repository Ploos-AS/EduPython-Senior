# M8.8 – Exercises and mini-project

Now you will use what you learned in M8 together.

The goal is not to learn many new Python features. The goal is to practise combining familiar parts.

## Exercise 1 – Read the whole file

Create a text file with three short lines.

Write a program that:

1. opens the file with \`"r"\`
2. uses UTF-8
3. reads all content with \`read()\`
4. prints the content

Explain to yourself why \`with open(...)\` is useful.

## Exercise 2 – Line by line

Create a file containing four integers, one per line.

Read the file with a \`for\` loop.

For each line:

1. use \`strip()\`
2. convert the text with \`int()\`
3. print the number

Also count how many numbers the file contains.

## Exercise 3 – Find the error

The program should read \`data/names.txt\`, but produces:

```text
FileNotFoundError
```

Investigate in this order:

1. the file name
2. the file extension
3. uppercase and lowercase letters
4. whether the \`data\` folder exists
5. which path the program is actually using

Do not add a general \`except\` merely to make the error message disappear.

## Exercise 4 – Write or append?

Choose the correct mode.

A. A report should be rebuilt completely each time.

B. A log should preserve old events and receive one new line.

C. An existing text file should only be read.

Answer with one of:

```text
"r"
"w"
"a"
```

Explain why.

## Exercise 5 – What is the result?

The file initially contains:

```text
Start
```

The program runs:

```python
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Check\n")

with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Finished\n")
```

Write down what you think the file contains afterwards.

Then run the program and check your answer.

## Exercise 6 – Functions

Create:

```python
def read_numbers(file_path):
    ...
```

The function should read one integer per line and return a list.

Then create:

```python
def calculate_total(numbers):
    ...
```

It should return the total without reading any file.

Why can it be useful for the calculation function not to know the file name?

# Mini-project – Measurement archive

We will create a small program that stores measurements over time.

The program uses a controlled text file that belongs to the project.

Each line contains one integer:

```text
12
15
11
14
```

## Part 1 – Locate the files

Use \`Path\`:

```python
from pathlib import Path

program_folder = Path(__file__).parent
data_file = program_folder / "data" / "measurements.txt"
report_file = program_folder / "report.txt"
```

## Part 2 – Read the history

Create:

```python
def read_measurements(file_path):
    ...
```

The function should:

- open the file with \`"r"\`
- read it line by line
- use \`strip()\`
- convert with \`int()\`
- add the values to a list
- return the list

## Part 3 – Add a new measurement

Create:

```python
def add_measurement(file_path, value):
    ...
```

Use \`"a"\`.

Remember that \`write()\` needs text and that each measurement should have its own line.

## Part 4 – Calculate

Create a function that calculates the total of the measurements.

You can also create a function that counts them with \`len()\`.

Keep the calculation separate from file reading.

## Part 5 – Write a report

Create:

```python
def write_report(file_path, count, total):
    ...
```

The report might look like:

```text
Number of measurements: 5
Total: 65
```

The report represents the current result, so it can be written with \`"w"\`.

The history file and report file therefore have different needs:

```text
measurements.txt → "a" → preserve history
report.txt       → "w" → rebuild current report
```

## Part 6 – Read the report back

Open the report file with \`"r"\` and print it.

This lets the program verify that the result was actually stored.

## Part 7 – Test deliberately

Test at least these situations:

- normal data file
- one new measurement
- run the append part once more
- incorrect data file name
- a line that cannot be converted to an integer

Read the error Python produces.

Then fix the cause.

## Debugging exercise

This program contains a logical error:

```python
def save(file_path, value):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(value) + "\n")
```

The program calls \`save()\` whenever a new historical measurement arrives.

Why do the old measurements disappear?

Which mode is more appropriate when the history should be preserved?

## Before moving on

You should now be able to explain the difference between:

```text
file contents
file path
working directory
program folder
"r"
"w"
"a"
read()
write()
FileNotFoundError
ValueError
```

You do not need to remember every piece of syntax by heart.

The important thing is that you recognise the parts, understand what they do, and know how to investigate an error.

## M8 complete

You have now moved from data that exists only while a program is running to programs that can store and retrieve data.

You can:

- read complete text files
- process files line by line
- write new files
- append history
- choose between \`"r"\`, \`"w"\`, and \`"a"\`
- read and understand common file errors
- use folders and relative paths
- build robust paths with \`Path\`
- combine files, lists, loops, and functions
- separate input, processing, and output/storage
- build a small program with persistent data

The next milestone is M9, where we work with structured tabular data and CSV.
