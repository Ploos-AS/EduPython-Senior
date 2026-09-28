# M8.1 – Why do programs need files?

So far, our programs have created data in variables, lists, and dictionaries.

But what happens when the program ends?

## Data in a program does not automatically persist

Look at:

```python
name = "Anna"
measurements = [12, 15, 11]

print(name)
print(measurements)
```

While the program runs, the values exist in the variables.

When the program finishes, those variables are not automatically saved for the next time the program starts.

If we want to keep data, we need somewhere to store it.

A common place is a **file**.

## A file can outlive the program

You already know files from other programs:

- text documents
- images
- spreadsheets
- PDF files
- music files

A Python program can also read and write files.

In this lesson, we will only **read** a text file supplied with the course.

We will not change or delete any files.

## The course file

The example uses the file:

```text
sample.txt
```

It contains ordinary text.

Think of it as a small note file for the program to read.

## Try it

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

When the example is run from the folder containing the file, Python opens \`sample.txt\`, reads the text, and stores it in the variable \`content\`.

The program then prints the text.

## Read the code in small parts

First:

```python
open("sample.txt", "r", encoding="utf-8")
```

This asks Python to open the file.

\`"sample.txt"\` is the file name.

\`"r"\` means **read**.

\`encoding="utf-8"\` tells Python how the text in the file is encoded.

UTF-8 can represent characters from many languages, including Norwegian letters such as æ, ø, and å.

## with open(...)

The complete beginning is:

```python
with open("sample.txt", "r", encoding="utf-8") as file:
```

While the indented part runs, we can use the file through the name \`file\`.

\`with\` also makes sure the file is closed correctly when the indented part is finished.

This will be our standard way to work with files.

You do not need to learn a separate \`close()\` rule first.

## read()

This line:

```python
content = file.read()
```

reads all the text content from the file.

The result is text, which means it is a string.

So \`content\` can be used like other text values you already know.

## Indentation matters again

Notice:

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

\`file.read()\` is inside the \`with\` block.

\`print(content)\` is after the block.

The file itself is closed by then, but the text we read is still stored in \`content\`.

## What does the file name mean?

```text
sample.txt
```

is a **path** to the file.

Here, the path is very simple: just the file name.

That means Python looks for the file in the program's current working directory.

We will learn more about folders and paths later in M8.

## If the file does not exist

If Python cannot find the file, you will usually get:

```text
FileNotFoundError
```

This does not mean Python is broken.

It means the program requested a file at a location where Python could not find it.

When you see this error, check:

1. the file name
2. the spelling
3. which folder the program is running from
4. whether the file actually exists there

We will return to this error later.

## Change it

Open the course file \`sample.txt\`.

Change some of the text, save it, and run the program again.

Notice that Python now reads the changed text.

Do not change the file name yet.

## Make it yourself

Create a new ordinary text file in the same folder as the program.

Write one or two lines in the file.

Then make a copy of the reading program and change the file name so that it reads your file.

Continue to use:

```python
"r"
```

so the program only opens the file for reading.

## What you learned

You can now:

- explain why files are used for data that should exist outside one program run
- open a text file for reading
- use \`with open(...)\`
- read the complete file with \`read()\`
- explain what \`"r"\` means
- recognise \`encoding="utf-8"\`
- understand that a simple file name is also a path
- recognise \`FileNotFoundError\`

The next lesson is about reading a text file one line at a time.
