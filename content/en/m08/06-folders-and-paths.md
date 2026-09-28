# M8.6 – Folders and relative paths

A file exists somewhere.

To open the correct file, a program needs to know its **path**.

So far, we have used simple paths such as:

\`\`\`text
sample.txt
\`\`\`

Now we will also use folders.

## A simple folder structure

Imagine that the project looks like this:

\`\`\`text
my-program/
├── program.py
└── data/
    └── places.txt
\`\`\`

The Python file is named \`program.py\`.

The text file is inside the \`data\` subfolder.

A relative path to the text file can be written as:

\`\`\`text
data/places.txt
\`\`\`

## What is a relative path?

A **relative path** describes a location relative to another location.

This:

\`\`\`text
data/places.txt
\`\`\`

roughly means:

> go to the \`data\` folder and find \`places.txt\`

But there is an important question:

**Relative to which folder?**

## The working directory

When Python starts a program, the process has a **current working directory**.

A simple call such as:

\`\`\`python
open("data/places.txt", "r", encoding="utf-8")
\`\`\`

is interpreted relative to that working directory.

The working directory is not necessarily the same folder that contains the Python file.

This is a common cause of \`FileNotFoundError\`.

## A more robust course pattern

Python includes the \`pathlib\` standard library module.

It provides \`Path\`.

\`\`\`python
from pathlib import Path
\`\`\`

We can find the folder containing the Python file itself:

\`\`\`python
program_folder = Path(__file__).parent
\`\`\`

You do not need to know every detail about \`__file__\` yet.

In this pattern, it simply means:

> start with the location of the Python file

## Build a path

We can combine folders and file names with \`/\`:

\`\`\`python
from pathlib import Path

program_folder = Path(__file__).parent
file_path = program_folder / "data" / "places.txt"
\`\`\`

This builds the path layer by layer:

\`\`\`text
program folder
    │
    └── data
         │
         └── places.txt
\`\`\`

Here, \`/\` does not mean division.

When we work with \`Path\`, it combines parts of a path.

## Read the file

\`\`\`python
from pathlib import Path

program_folder = Path(__file__).parent
file_path = program_folder / "data" / "places.txt"

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
\`\`\`

The program now finds the data file based on where \`program.py\` is located, rather than the working directory from which Python happened to be started.

## Why is this useful?

Imagine that the program is located at:

\`\`\`text
course/m08/program.py
\`\`\`

You may start it from different locations.

If the file path is built from \`Path(__file__).parent\`, the program can still find the data file stored beside it in the project structure.

This makes examples and small projects more predictable.

## Path is a path value

The variable:

\`\`\`python
file_path = program_folder / "data" / "places.txt"
\`\`\`

contains a \`Path\` object.

\`open()\` can use it directly:

\`\`\`python
open(file_path, "r", encoding="utf-8")
\`\`\`

We do not need to convert the path to text first.

## parent

In:

\`\`\`python
Path(__file__).parent
\`\`\`

\`.parent\` means the folder containing the file.

If the Python file is:

\`\`\`text
/home/anna/course/program.py
\`\`\`

the parent folder is:

\`\`\`text
/home/anna/course
\`\`\`

The exact path will naturally be different on different computers.

That is exactly why we do not put one particular user's complete path into the program.

## Avoid hard-coded personal paths

This may work on one particular computer:

\`\`\`python
open("/home/anna/course/data/places.txt", "r", encoding="utf-8")
\`\`\`

but the program becomes tied to that location.

On another computer, the user name, operating system, or folder structure may be different.

When the data file belongs with the program, it is often better to build the path relative to the program file.

## Folders can also be missing

If we build:

\`\`\`python
file_path = program_folder / "data" / "places.txt"
\`\`\`

but the \`data\` folder or file does not exist, reading can still produce:

\`\`\`text
FileNotFoundError
\`\`\`

A valid Python path can still point to something that does not exist.

Use the debugging knowledge from M8.5.

## Change it

Create this structure:

\`\`\`text
practice/
├── program.py
└── data/
    └── names.txt
\`\`\`

Put a few names in \`names.txt\`.

Use:

\`\`\`python
from pathlib import Path

program_folder = Path(__file__).parent
file_path = program_folder / "data" / "names.txt"
\`\`\`

Read the file line by line.

## Make it yourself

Create a new subfolder beside the program, for example:

\`\`\`text
notes/
\`\`\`

Put a text file in that folder.

Build the path with \`Path(__file__).parent\` and \`/\`.

The program should:

1. build the path
2. open the file with \`"r"\`
3. read it line by line
4. use \`strip()\`
5. print the contents

## What you learned

You can now:

- explain what a folder and file path describe
- recognise a relative path
- understand that the working directory and program folder can differ
- import \`Path\` from \`pathlib\`
- find the program folder with \`Path(__file__).parent\`
- build a path with \`/\`
- pass a \`Path\` directly to \`open()\`
- avoid hard-coding one user's complete path
- use your \`FileNotFoundError\` knowledge when a folder or file is missing

The next lesson combines files with lists and functions.
