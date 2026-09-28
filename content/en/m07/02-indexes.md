# M7.2 – Retrieve one value from a list

A list can contain many values. Sometimes we want to retrieve only one of them.

We use the value's **index**.

## Try it

\`\`\`python
days = ["Monday", "Tuesday", "Wednesday"]

print(days[0])
\`\`\`

Result:

\`\`\`text
Monday
\`\`\`

\`[0]\` means: retrieve the first value in the list.

## Python starts at 0

This is important:

| Position | Index | Value |
|---|---:|---|
| first | 0 | Monday |
| second | 1 | Tuesday |
| third | 2 | Wednesday |

Therefore:

\`\`\`python
print(days[0])
print(days[1])
print(days[2])
\`\`\`

gives:

\`\`\`text
Monday
Tuesday
Wednesday
\`\`\`

## Why does it start at 0?

In Python, as in many programming languages, the index is a position counted from the start of the collection.

The first value is **0 steps from the start**.

The next is 1 step from the start.

You do not need to spend time liking this convention. The important thing to remember is:

> The first value has index 0.

## See the list as two rows

\`\`\`text
index:    0          1          2
value:   Monday     Tuesday    Wednesday
\`\`\`

When you write:

\`\`\`python
days[1]
\`\`\`

Python looks at index 1 and finds \`"Tuesday"\`.

## Index is not the same as count

The list contains three values:

\`\`\`python
days = ["Monday", "Tuesday", "Wednesday"]
\`\`\`

But the final index is 2.

That is because the indexes are:

\`\`\`text
0, 1, 2
\`\`\`

This is a common source of errors when learning programming.

## What happens when an index does not exist?

Try:

\`\`\`python
days = ["Monday", "Tuesday", "Wednesday"]

print(days[3])
\`\`\`

Python reports an error containing:

\`\`\`text
IndexError: list index out of range
\`\`\`

This means the program tried to retrieve a position that does not exist in the list.

The list has three values, but its valid indexes are 0, 1, and 2.

## Read the error message

When you see:

\`\`\`text
IndexError
\`\`\`

ask:

1. Which list am I using?
2. Which index am I trying to retrieve?
3. How many values are in the list?
4. Did I start counting at 0?

The error message is information that helps us find the problem.

## Use a variable as an index

The index does not have to be written directly inside the brackets:

\`\`\`python
days = ["Monday", "Tuesday", "Wednesday"]
index = 1

print(days[index])
\`\`\`

The result is:

\`\`\`text
Tuesday
\`\`\`

Python uses the value in \`index\`, which is 1.

## Change it

Start with:

\`\`\`python
places = ["Tonstad", "Grimstad", "Oslo", "Bergen"]
\`\`\`

Print:

- the first value
- the second value
- the fourth value

Predict the indexes before running the program.

## Make it yourself

Create a list with at least five values.

Print:

- the first value
- a value from the middle
- the last value using its explicit index

Then deliberately try an index that is too large. Read the \`IndexError\`, correct the index, and run the program again.

## What you learned

You can now:

- retrieve one list item using an index
- explain that the first index is 0
- distinguish the number of items from the final index
- use a variable as an index
- recognise and investigate \`IndexError: list index out of range\`

The next lesson is about changing a list and adding new values.
