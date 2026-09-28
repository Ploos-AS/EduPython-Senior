# M7.7 – Combine lists and dictionaries

We have learned that:

- a list collects several values in an order
- a dictionary collects named information about one thing

Now we combine them.

## The problem

Imagine that we want to store several electricity measurements.

One measurement can be described like this:

\`\`\`python
measurement = {
    "day": "Monday",
    "kwh": 12.4
}
\`\`\`

But we have several days.

We can create a **list of dictionaries**.

## Try it

\`\`\`python
measurements = [
    {"day": "Monday", "kwh": 12.4},
    {"day": "Tuesday", "kwh": 10.8},
    {"day": "Wednesday", "kwh": 13.1}
]

print(measurements)
\`\`\`

The outer structure is a list:

\`\`\`text
[ ... ]
\`\`\`

Each item in the list is a dictionary:

\`\`\`text
{ ... }
\`\`\`

## See the structure layer by layer

\`\`\`text
list
│
├── dictionary: day → Monday,    kwh → 12.4
├── dictionary: day → Tuesday,   kwh → 10.8
└── dictionary: day → Wednesday, kwh → 13.1
\`\`\`

We do not need to understand everything at once.

First, we retrieve one item from the list.

## Retrieve one dictionary from the list

\`\`\`python
first = measurements[0]

print(first)
\`\`\`

The result is the first dictionary:

\`\`\`text
{'day': 'Monday', 'kwh': 12.4}
\`\`\`

Now we can retrieve a value from it:

\`\`\`python
print(first["day"])
print(first["kwh"])
\`\`\`

## Two steps

This:

\`\`\`python
first = measurements[0]
print(first["day"])
\`\`\`

does two things:

1. retrieve item 0 from the list
2. retrieve the value with key \`"day"\` from the dictionary

We can write this more compactly later, but two steps make the data structure easier to follow.

## Go through all entries

We already know \`for\`:

\`\`\`python
for measurement in measurements:
    print(measurement)
\`\`\`

During each iteration, \`measurement\` refers to one dictionary.

Therefore we can write:

\`\`\`python
for measurement in measurements:
    print(measurement["day"], measurement["kwh"])
\`\`\`

Result:

\`\`\`text
Monday 12.4
Tuesday 10.8
Wednesday 13.1
\`\`\`

## Follow the loop

First iteration:

\`\`\`python
measurement = {"day": "Monday", "kwh": 12.4}
\`\`\`

Second iteration:

\`\`\`python
measurement = {"day": "Tuesday", "kwh": 10.8}
\`\`\`

Third iteration:

\`\`\`python
measurement = {"day": "Wednesday", "kwh": 13.1}
\`\`\`

It is the same \`for\` idea as before. The only new part is that each value in the list is now a dictionary.

## Calculate with the values

We can add the measurements:

\`\`\`python
total = 0

for measurement in measurements:
    total = total + measurement["kwh"]

print("Total:", total)
\`\`\`

Here we combine:

- list
- dictionary
- \`for\`
- variable
- calculation

Each part is already familiar on its own.

## Use a function

We can move the calculation into a function:

\`\`\`python
def calculate_total(measurements):
    total = 0

    for measurement in measurements:
        total = total + measurement["kwh"]

    return total
\`\`\`

And use it like this:

\`\`\`python
total = calculate_total(measurements)
print("Total:", total)
\`\`\`

The function receives the complete list.

The loop visits the dictionaries one at a time.

## Add a new entry

We already know \`append()\`:

\`\`\`python
new_measurement = {
    "day": "Thursday",
    "kwh": 11.7
}

measurements.append(new_measurement)
\`\`\`

The list now contains four dictionaries.

We are using the same operations as before. The values have simply become more structured.

## Change it

Start with three measurements.

1. Change one \`kwh\` value.
2. Add a fourth measurement with \`append()\`.
3. Use a \`for\` loop to print the day and kWh.
4. Calculate the total.

You can follow the contents of the list after each change.

## Make it yourself

Create a list with at least three dictionaries describing the same kind of thing.

For example:

- books with a title and page count
- appointments with a day and time
- places with a name and temperature
- expenses with a description and amount

Create a function that receives the list and uses at least one value from each dictionary.

## What you learned

You can now:

- explain what a list of dictionaries is
- read a compound data structure layer by layer
- retrieve one dictionary from a list
- retrieve a value from that dictionary
- visit several dictionaries with \`for\`
- calculate with values from the dictionaries
- pass a list of dictionaries to a function
- add a new structured entry with \`append()\`

This pattern will become important later when we work with tables and CSV files.

The next lesson brings M7 together with exercises and debugging.
