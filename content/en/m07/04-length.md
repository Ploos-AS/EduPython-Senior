# M7.4 – How long is the list?

We often need to know how many items a list contains.

Python has the \`len()\` function.

## Try it

\`\`\`python
temperatures = [18, 20, 17, 21]

count = len(temperatures)

print("Count:", count)
\`\`\`

Result:

\`\`\`text
Count: 4
\`\`\`

\`len\` is short for *length*.

## len() gives the number of items

The list:

\`\`\`python
temperatures = [18, 20, 17, 21]
\`\`\`

contains four items.

Therefore:

\`\`\`python
len(temperatures)
\`\`\`

gives \`4\`.

## Count and final index are different

This is important.

For the list:

\`\`\`python
days = ["Monday", "Tuesday", "Wednesday"]
\`\`\`

we have:

\`\`\`text
number of items: 3
valid indexes:   0, 1, 2
final index:     2
\`\`\`

So:

\`\`\`python
len(days)
\`\`\`

gives 3, while:

\`\`\`python
days[2]
\`\`\`

retrieves the final item.

## The final index with len()

When the list is not empty, the final valid index is:

\`\`\`python
len(days) - 1
\`\`\`

Example:

\`\`\`python
days = ["Monday", "Tuesday", "Wednesday"]

last_index = len(days) - 1

print(days[last_index])
\`\`\`

Result:

\`\`\`text
Wednesday
\`\`\`

Later, we will learn a shorter Python way to retrieve the final item. For now, this makes the relationship between length and index clear.

## What about an empty list?

\`\`\`python
values = []

print(len(values))
\`\`\`

Result:

\`\`\`text
0
\`\`\`

An empty list has length 0.

But it has no valid index.

If we calculate:

\`\`\`python
len(values) - 1
\`\`\`

we get \`-1\`, but this does not mean that the list suddenly contains an item.

We will learn more about negative indexes later.

## Check before retrieving

We can use what we learned about \`if\`:

\`\`\`python
values = []

if len(values) > 0:
    last_index = len(values) - 1
    print(values[last_index])
else:
    print("The list is empty.")
\`\`\`

Result:

\`\`\`text
The list is empty.
\`\`\`

The program now tries to retrieve an item only when the list actually contains something.

## len() after append()

The length changes when we add values:

\`\`\`python
measurements = []

print(len(measurements))

measurements.append(12)
print(len(measurements))

measurements.append(15)
print(len(measurements))
\`\`\`

Result:

\`\`\`text
0
1
2
\`\`\`

This shows that the list changes while the program runs.

## Use len() in a function

\`\`\`python
def show_count(values):
    print("The list has", len(values), "items.")

show_count([10, 20, 30])
\`\`\`

Result:

\`\`\`text
The list has 3 items.
\`\`\`

Here we combine lists with functions from M6.

## Change it

Start with:

\`\`\`python
places = ["Tonstad", "Grimstad", "Oslo", "Bergen"]
\`\`\`

Print:

- the complete list
- the number of items
- the final valid index
- the item at the final valid index

Then add another place with \`append()\` and do the same again.

## Make it yourself

Create a list with at least five values.

Use \`len()\` to find the count.

Then create an empty list and use \`if\` to check that it contains at least one item before trying to retrieve the final one.

## What you learned

You can now:

- use \`len()\` to find the number of items
- distinguish item count from the final index
- find the final index of a non-empty list with \`len(list_name) - 1\`
- explain why an empty list needs extra care
- use \`if\` before retrieving an item
- see that the length changes when the list changes
- use \`len()\` together with functions

The next lesson introduces dictionaries: collections where we find values using names instead of numbered positions.
