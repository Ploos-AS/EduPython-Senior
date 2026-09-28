# M8.2 – Read a file line by line

In the previous lesson, we used \`read()\` to read the complete file at once.

Often, we want to process one line at a time instead.

We can use a \`for\` loop.

## Try it

Imagine that \`temperatures.txt\` contains:

\`\`\`text
18
20
17
21
\`\`\`

The program can read the lines like this:

\`\`\`python
with open("temperatures.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
\`\`\`

This uses the same \`for\` idea that you already know.

Python gives us one line from the file at a time.

## Follow the loop

First iteration:

\`\`\`text
line → "18" + newline
\`\`\`

Second iteration:

\`\`\`text
line → "20" + newline
\`\`\`

and this continues until the file has been read.

\`\n\` represents a newline.

You normally do not see the characters \`\`\\n\`\` in the text file. They describe the end of one line and the start of another.

## Why can print() add extra space?

\`print()\` normally adds its own newline.

If the text we print already ends with a newline, the result can look like:

\`\`\`text
18

20

17

21
\`\`\`

We can remove the newline before printing the text.

## strip()

\`\`\`python
with open("temperatures.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        print(line)
\`\`\`

Now the result is:

\`\`\`text
18
20
17
21
\`\`\`

\`strip()\` creates a text value without whitespace and newlines at the beginning and end.

In this example, we mainly use it to remove the newline.

## File → line → text

It can help to think like this:

\`\`\`text
text file
   │
   ├── line 1 → "18"
   ├── line 2 → "20"
   ├── line 3 → "17"
   └── line 4 → "21"
\`\`\`

The loop processes one text line at a time.

## Numbers in a text file are still text

Even if the file contains:

\`\`\`text
18
20
17
\`\`\`

each line is read as text.

If we want to calculate with the value, we must convert it:

\`\`\`python
with open("temperatures.txt", "r", encoding="utf-8") as file:
    for line in file:
        temperature = int(line.strip())
        print(temperature + 1)
\`\`\`

This builds on the conversion you learned earlier.

## Calculate a sum

We can combine a file, loop, and accumulator:

\`\`\`python
total = 0

with open("temperatures.txt", "r", encoding="utf-8") as file:
    for line in file:
        value = int(line.strip())
        total = total + value

print("Total:", total)
\`\`\`

For the file:

\`\`\`text
18
20
17
21
\`\`\`

the total is:

\`\`\`text
Total: 76
\`\`\`

## Why read line by line?

\`read()\` is simple when we want the complete text.

A \`for\` loop is useful when we want to:

- process each line separately
- convert each line
- count lines
- look for particular values
- calculate something from the data

Later, this will be important when we work with data files.

## Count the lines

\`\`\`python
count = 0

with open("temperatures.txt", "r", encoding="utf-8") as file:
    for line in file:
        count = count + 1

print("Number of lines:", count)
\`\`\`

Here, we do not even need the contents of the line. We only count how many times the loop runs.

## Change it

Use a text file containing at least four numbers.

Create a program that:

1. reads the file line by line
2. uses \`strip()\`
3. converts each line to \`int\`
4. prints each number
5. calculates the total

Then change one number in the file and run the program again.

## Make it yourself

Create a text file with one name or place on each line.

Write a program that:

- reads the file line by line
- removes the newline with \`strip()\`
- prints each value
- counts how many lines the file contains

## What you learned

You can now:

- read a text file line by line
- use a file directly in a \`for\` loop
- understand that text lines normally contain newlines
- use \`strip()\`
- convert text from a file to numbers
- calculate a sum from file contents
- count lines
- choose between \`read()\` and line-by-line processing

The next lesson is about writing a new text file.
