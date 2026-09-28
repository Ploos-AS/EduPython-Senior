# M8.7 – Files, lists, and functions

We have now learned to:

- read files
- write files
- add data with append
- use folders and paths
- use lists
- create functions

Now we put the pieces together.

## A clear data flow

A useful pattern is:

\`\`\`text
file
 ↓
reading function
 ↓
list
 ↓
processing
 ↓
result
 ↓
writing function
 ↓
new file
\`\`\`

Each part has one clear job.

## The data file

Imagine that \`measurements.txt\` contains:

\`\`\`text
12
15
11
14
\`\`\`

We want to:

1. read the numbers
2. store them in a list
3. calculate the total
4. write the result to a new file

## Read the file into a list

\`\`\`python
def read_measurements(file_path):
    measurements = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            value = int(line.strip())
            measurements.append(value)

    return measurements
\`\`\`

Follow the data:

First:

\`\`\`python
measurements = []
\`\`\`

After the first line:

\`\`\`python
measurements = [12]
\`\`\`

After the second:

\`\`\`python
measurements = [12, 15]
\`\`\`

Finally:

\`\`\`python
measurements = [12, 15, 11, 14]
\`\`\`

The function returns the list.

## The file path is a parameter

Notice:

\`\`\`python
def read_measurements(file_path):
\`\`\`

The function does not decide on one specific file name itself.

It receives the path as an argument.

That makes the function easier to reuse with other practice files later.

## Calculate with the list

File handling does not need to be part of the calculation.

\`\`\`python
def calculate_total(measurements):
    total = 0

    for measurement in measurements:
        total = total + measurement

    return total
\`\`\`

This function knows nothing about files.

It receives a list and returns a number.

That makes the responsibilities clear:

\`\`\`text
read_measurements() → file to list
calculate_total()   → list to number
\`\`\`

## Write the result

\`\`\`python
def write_result(file_path, total):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Total: " + str(total) + "\n")
\`\`\`

This function has another responsibility:

\`\`\`text
write_result() → value to file
\`\`\`

## Put the pieces together

With \`Path\`, the main part of the program can look like:

\`\`\`python
from pathlib import Path

program_folder = Path(__file__).parent
input_file = program_folder / "data" / "measurements.txt"
output_file = program_folder / "result.txt"

measurements = read_measurements(input_file)
total = calculate_total(measurements)
write_result(output_file, total)

print("Measurements:", measurements)
print("Total:", total)
\`\`\`

The data flow is:

\`\`\`text
measurements.txt
       ↓
[12, 15, 11, 14]
       ↓
52
       ↓
result.txt
\`\`\`

## Why use several functions?

We could write everything in one long block.

But separate functions make it easier to answer:

- Where is the file read?
- Where are the lines converted to numbers?
- Where is the total calculated?
- Where is the result written?

If the total is wrong, we can inspect \`calculate_total()\`.

If the file cannot be found, we can inspect the path and \`read_measurements()\`.

This makes debugging easier.

## Check intermediate results

We can print the list before calculating:

\`\`\`python
measurements = read_measurements(input_file)
print(measurements)
\`\`\`

If the result is:

\`\`\`text
[12, 15, 11, 14]
\`\`\`

we know that the reading and conversion look correct.

Then we can inspect the next step.

This is a useful way to debug a data flow: check one intermediate result at a time.

## What if one line is not a number?

If the file contains:

\`\`\`text
12
fifteen
11
\`\`\`

then:

\`\`\`python
int("fifteen")
\`\`\`

produces \`ValueError\`.

That is not a file error.

The file was found and read, but its contents did not have the format the program expected.

This shows why it is useful to read the actual error type.

We do not add a broad \`except\` to hide the problem.

## Change it

Use a file containing four integers.

1. Read them into a list with a function.
2. Print the list.
3. Calculate the total in another function.
4. Change one number in the data file.
5. Run the program again and follow how the result changes.

## Make it yourself

Create a small program with three functions:

\`\`\`python
def read_data(file_path):
    ...

def calculate(data):
    ...

def write_result(file_path, result):
    ...
\`\`\`

Use your own practice file with one integer per line.

The program should:

1. build input and output paths with \`Path\`
2. read the numbers into a list
3. perform a simple calculation
4. write the result to a dedicated result file
5. print the result to the screen

Only use a controlled practice file as the output file.

## What you learned

You can now:

- read file contents into a list
- pass a file path to a function
- return a list from a function
- separate file input from calculation
- write a calculated result to a new file
- build a simple data flow from file to Python data and back to a file
- check intermediate results while debugging
- distinguish \`FileNotFoundError\` from \`ValueError\`

The next lesson brings M8 together with exercises, debugging, and a mini-project.
