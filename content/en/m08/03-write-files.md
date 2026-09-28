# M8.3 – Write a text file

We have read files.

Now the program will create a file.

## Important before we begin

When we open a file with:

\`\`\`python
"w"
\`\`\`

it means **write**.

If the file does not exist, it is created.

If the file already exists, its old contents are replaced.

For that reason, this lesson only uses a dedicated course file that is safe to create again.

Do not use the name of an important document when experimenting with \`"w"\`.

## Try it

\`\`\`python
with open("result.txt", "w", encoding="utf-8") as file:
    file.write("This was written by Python.\n")
\`\`\`

When the program finishes, \`result.txt\` exists.

Open it in a text editor.

You should see:

\`\`\`text
This was written by Python.
\`\`\`

## The same pattern as reading

For reading, we used:

\`\`\`python
with open("sample.txt", "r", encoding="utf-8") as file:
\`\`\`

For writing, we use:

\`\`\`python
with open("result.txt", "w", encoding="utf-8") as file:
\`\`\`

The difference is the mode:

\`\`\`text
"r" → read
"w" → write
\`\`\`

## write()

This line:

\`\`\`python
file.write("This was written by Python.\n")
\`\`\`

writes text to the file.

Notice \`\n\`.

\`write()\` does not automatically add a newline in the way that \`print()\` normally does.

If we want a new line, we therefore write the newline ourselves.

## Write several lines

\`\`\`python
with open("result.txt", "w", encoding="utf-8") as file:
    file.write("Monday\n")
    file.write("Tuesday\n")
    file.write("Wednesday\n")
\`\`\`

The file becomes:

\`\`\`text
Monday
Tuesday
Wednesday
\`\`\`

## Write values from a list

We can combine file writing with what we learned in M7:

\`\`\`python
places = ["Tonstad", "Grimstad", "Oslo"]

with open("places.txt", "w", encoding="utf-8") as file:
    for place in places:
        file.write(place + "\n")
\`\`\`

Each item is now written on its own line.

## Numbers must become text

\`write()\` writes text.

This does not work:

\`\`\`python
count = 3
file.write(count)
\`\`\`

We must convert the number:

\`\`\`python
count = 3
file.write(str(count))
\`\`\`

This is the same idea as before: Python distinguishes numbers from text.

## Write and read back

A useful way to check a small program is:

1. write the file
2. open it for reading
3. inspect what was actually stored

\`\`\`python
with open("result.txt", "w", encoding="utf-8") as file:
    file.write("Line one\n")
    file.write("Line two\n")

with open("result.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
\`\`\`

The first \`with\` block writes.

The second reads.

## What if the file already exists?

Imagine that \`result.txt\` contains:

\`\`\`text
Old text
\`\`\`

Then we run:

\`\`\`python
with open("result.txt", "w", encoding="utf-8") as file:
    file.write("New text\n")
\`\`\`

Afterwards, the file contains:

\`\`\`text
New text
\`\`\`

The old text is gone.

That is why we must know which file we are opening before using \`"w"\`.

## A simple safety rule

While learning:

**Use \`"w"\` only on files you created for the exercise.**

We will not write to documents, images, configuration files, or other important files.

Later, we will learn how to add content without replacing what is already there.

## Change it

Create a list:

\`\`\`python
tasks = ["Shopping", "Call the bank", "Read"]
\`\`\`

Write each item to \`tasks.txt\`, one item per line.

Open the file afterwards and inspect its contents.

Then change the list and run the program again.

Notice that the file is rebuilt from the list.

## Make it yourself

Create a program that:

1. has a list containing at least three text values
2. opens a new practice file with \`"w"\`
3. uses a \`for\` loop
4. writes one value per line
5. opens the file again with \`"r"\`
6. prints the stored contents

Only use a file that you created specifically for the exercise.

## What you learned

You can now:

- open a file with \`"w"\`
- explain that \`"w"\` creates or replaces a file
- write text with \`write()\`
- add newlines with \`\n\`
- convert numbers to text before writing
- write items from a list
- read a written file back for verification
- explain why the file name must be checked before using \`"w"\`

The next lesson is about adding new data without replacing the existing contents.
