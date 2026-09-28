# M8.5 – File errors and debugging

When we work with files, a program may request a file that is not where we expect it to be.

Python tells us about this with an error message.

The goal is not to avoid every error. The goal is to read errors and find their cause.

## FileNotFoundError

This program tries to read a file:

```python
with open("measurements.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

If Python cannot find the file, the error message can contain:

```text
FileNotFoundError
```

The name tells us a lot:

```text
File     Not Found     Error
```

The program requested a file that Python could not find at the specified path.

## Check the simple things first

When you see \`FileNotFoundError\`, check:

1. Is the file name correct?
2. Is the extension correct, such as \`.txt\`?
3. Is the capitalization correct?
4. Does the file actually exist?
5. Is the program running from the folder you expect?

A small spelling error is enough:

```python
open("temperature.txt", "r", encoding="utf-8")
```

if the file is actually named:

```text
temperatures.txt
```

## The path is part of the error

Python does not search for the file “everywhere”.

The file name or path tells Python where the program expects to find it.

A simple name:

```text
temperatures.txt
```

is a relative path.

It is interpreted relative to the program's **current working directory**.

That is why the same code may find a file in one situation and fail in another if the working directory changes.

We will learn more about folders and paths in the next lesson.

## Read the complete error message

Do not stop at the word \`Error\`.

Look for:

- the type of error
- the file name Python tried to open
- the line in the program where the error occurred

The error message is information for you.

## When the error is expected

Some programs need to handle a missing file.

Then we can use \`try\` and \`except\`.

```python
try:
    with open("notes.txt", "r", encoding="utf-8") as file:
        content = file.read()

    print(content)
except FileNotFoundError:
    print("Could not find notes.txt")
```

Python first tries the code under \`try\`.

If specifically a \`FileNotFoundError\` occurs, Python runs the code under:

```python
except FileNotFoundError:
```

## Why do we name the error type?

We use:

```python
except FileNotFoundError:
```

rather than a general rule that hides every error.

If the program contains another error, we still want to see it so that we can fix it.

That is useful while learning and in real programs.

## Do not use except to hide a spelling mistake

If the file is supposed to exist but you typed the wrong name, the best solution is usually to correct the file name.

\`try/except\` is useful when a missing file is a situation the program genuinely expects.

Ask:

**Is it normal for this file to be missing?**

If not, investigate why it is missing.

## A function that reads a file

We can combine this with functions:

```python
def read_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "No notes file found."
```

The function returns either the file contents or a clear message.

## Other file errors also exist

Files can produce other errors, for example when a program does not have permission to read or write somewhere.

We do not need to learn every error type now.

The important points are:

- read the error Python actually shows
- do not assume every file problem is \`FileNotFoundError\`
- do not hide unknown errors with an overly broad \`except\`

## Change it

Make a copy of a reading program.

1. First use the correct file name.
2. Change one letter in the file name.
3. Run the program and read the \`FileNotFoundError\`.
4. Correct the file name.
5. Then add \`try/except FileNotFoundError\` and try a missing file name again.

Compare an unhandled error with an expected error that the program handles.

## Make it yourself

Create a function that tries to read your own practice file.

If the file exists, the function should return its contents.

If the file is missing, it should return a short, understandable message.

Use only:

```python
except FileNotFoundError:
```

not a general \`except\`.

## What you learned

You can now:

- recognise \`FileNotFoundError\`
- check file names, extensions, and locations
- understand that relative paths depend on the working directory
- use an error message as information
- distinguish an error that should be fixed from an expected situation
- use \`try/except FileNotFoundError\`
- understand why we do not hide every error with a general \`except\`

The next lesson is about folders and relative paths.
