# M8.4 – Add text with append

In the previous lesson, we used:

```python
"w"
```

That creates or replaces a file.

Sometimes we want to keep what is already in the file and add something new.

Then we can use:

```python
"a"
```

\`"a"\` means **append** – add at the end.

## Try it

First, create a practice file:

```python
with open("log.txt", "w", encoding="utf-8") as file:
    file.write("Program started\n")
```

Then open it with \`"a"\`:

```python
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("First task completed\n")
```

The file now contains:

```text
Program started
First task completed
```

The first line was preserved.

## Three modes

We now know three file modes:

```text
"r" → read   → read existing content
"w" → write  → write and replace old content
"a" → append → add after existing content
```

It is important to choose the correct mode before opening the file.

## Append several times

```python
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Second task completed\n")

with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Program ending\n")
```

The file now contains several entries.

Each use of \`"a"\` adds new text at the end.

## Remember the newline

This:

```python
file.write("New entry")
```

does not automatically add a newline.

If the next entry also lacks the newline escape sequence, the result can be:

```text
New entryNext entry
```

For one entry per line, use:

```python
file.write("New entry\n")
```

## Append also creates the file

If the file does not exist, \`"a"\` will normally create it.

That means:

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("First note\n")
```

can be used even if \`notes.txt\` did not already exist.

The difference from \`"w"\` matters when the file already exists:

- \`"w"\` replaces the contents
- \`"a"\` preserves the contents and adds new data

## A small logging pattern

A log is a file where new events are added over time.

```python
def add_log(message):
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(message + "\n")
```

We can call the function several times:

```python
add_log("Start")
add_log("Check completed")
add_log("Finished")
```

This combines M6 functions with M8 files.

## Read the log back

```python
with open("log.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

We are now combining three earlier ideas:

- append to store new entries
- read to retrieve them
- for to process one line at a time

## When is "a" useful?

Append is useful when each new entry should follow the old entries.

Examples include:

- a simple log
- a list of new notes
- measurements recorded over time
- a simple history

But append is not appropriate if the whole file represents one updated version of some data.

In that case, rebuilding the contents and writing a new file with \`"w"\` may be better.

## Do not use append blindly

If you run this program three times:

```python
with open("log.txt", "a", encoding="utf-8") as file:
    file.write("Program ran\n")
```

you get three new lines.

That is correct if you want history.

It is wrong if you expected the file to contain only one line.

So ask:

**Should the old contents be preserved?**

If yes, \`"a"\` may be appropriate.

## Change it

First create \`notes.txt\` with \`"w"\` and one line.

Then add two new lines with \`"a"\`.

Read the file back and check that all three lines are present.

Run the append part once more and see what happens.

## Make it yourself

Create a function:

```python
def add_note(note):
    # write the note to the file
```

The function should:

1. open a dedicated practice file with \`"a"\`
2. write the note
3. add the newline escape sequence

Call the function at least three times.

Then read the file line by line and print the notes.

## What you learned

You can now:

- explain the difference between \`"r"\`, \`"w"\`, and \`"a"\`
- add text without replacing existing contents
- understand that append can also create a file
- use newlines between entries
- create a simple logging function
- read an appended file back
- choose between replacing and preserving old contents

The next lesson looks more systematically at file errors and how to understand them.
