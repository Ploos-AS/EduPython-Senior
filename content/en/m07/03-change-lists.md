# M7.3 – Change a list

Lists can be changed after they are created.

We will begin with two common operations:

1. replace a value that already exists
2. add a new value at the end

## Try it – replace a value

\`\`\`python
temperatures = [18, 20, 17]

temperatures[1] = 21

print(temperatures)
\`\`\`

Result:

\`\`\`text
[18, 21, 17]
\`\`\`

Index 1 was the second value.

We replaced 20 with 21.

## Read the assignment

This line:

\`\`\`python
temperatures[1] = 21
\`\`\`

can be read as:

> set the value at index 1 in temperatures to 21

We use the same index model as in the previous lesson:

\`\`\`text
index:      0    1    2
before:    18   20   17
after:     18   21   17
\`\`\`

It is the same list, but its contents have changed.

## The index must exist

If the list is:

\`\`\`python
temperatures = [18, 20, 17]
\`\`\`

we can change index 0, 1, or 2.

This does not work:

\`\`\`python
temperatures[3] = 25
\`\`\`

Python reports:

\`\`\`text
IndexError: list assignment index out of range
\`\`\`

Index 3 does not exist yet.

To add a new value, we use \`append()\`.

## Add with append

\`\`\`python
temperatures = [18, 20, 17]

temperatures.append(21)

print(temperatures)
\`\`\`

Result:

\`\`\`text
[18, 20, 17, 21]
\`\`\`

\`append()\` adds one new value to the end of the list.

## The dot means we do something with the list

Look at:

\`\`\`python
temperatures.append(21)
\`\`\`

Here we ask the \`temperatures\` list to perform the \`append\` operation.

Python has many such operations for lists. They are called **methods**.

You do not need to learn many methods now. In this lesson, we only use \`append()\`.

## Start with an empty list

A list can be built over time:

\`\`\`python
measurements = []

measurements.append(12)
measurements.append(15)
measurements.append(11)

print(measurements)
\`\`\`

Result:

\`\`\`text
[12, 15, 11]
\`\`\`

This is useful when we do not know all the values when the program starts.

## Build a list in a loop

We can combine \`append()\` with \`for\`:

\`\`\`python
doubled_numbers = []

for number in [2, 4, 6]:
    doubled_numbers.append(number * 2)

print(doubled_numbers)
\`\`\`

Result:

\`\`\`text
[4, 8, 12]
\`\`\`

Follow the list:

\`\`\`text
start:       []
after 2:     [4]
after 4:     [4, 8]
after 6:     [4, 8, 12]
\`\`\`

The list changes during each loop iteration.

## Replace or add?

Use:

\`\`\`python
list_name[index] = value
\`\`\`

when you want to **replace a value at a position that already exists**.

Use:

\`\`\`python
list_name.append(value)
\`\`\`

when you want to **add a new value at the end**.

## Change it

Start with:

\`\`\`python
places = ["Tonstad", "Grimstad", "Oslo"]
\`\`\`

Replace the second value with another place.

Then add a fourth place with \`append()\`.

Print the list after each change.

## Make it yourself

Start with an empty list.

Add at least four related values using \`append()\`.

Then change one of the values using an index.

Use a \`for\` loop to print the completed list one value at a time.

## What you learned

You can now:

- replace an existing list item
- explain that an index must exist before it can be replaced
- recognise \`IndexError\` from an invalid assignment
- add a value with \`append()\`
- explain simply what a list method is
- build up an empty list
- use \`append()\` in a loop
- choose between replacing and adding

The next lesson is about finding how many items a list contains and using its length safely.
