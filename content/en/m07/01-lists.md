# M7.1 – Several values in a list

Until now, our variables have usually held one value:

\`\`\`python
temperature = 18
\`\`\`

But what if we have several temperature readings?

We could create many variables:

\`\`\`python
temperature1 = 18
temperature2 = 20
temperature3 = 17
temperature4 = 21
\`\`\`

That works for four readings, but quickly becomes inconvenient.

Python has **lists** for collections of values that belong together.

## Try it

\`\`\`python
temperatures = [18, 20, 17, 21]

print(temperatures)
\`\`\`

The result is:

\`\`\`text
[18, 20, 17, 21]
\`\`\`

The variable \`temperatures\` now contains a **list** with four values.

## Square brackets create the list

A list is written with \`[\` and \`]\`.

The values are separated by commas:

\`\`\`python
temperatures = [18, 20, 17, 21]
\`\`\`

You can read this as:

> temperatures is a list containing 18, 20, 17, and 21

## A list can contain text

\`\`\`python
places = ["Tonstad", "Kristiansand", "Oslo"]

print(places)
\`\`\`

Result:

\`\`\`text
['Tonstad', 'Kristiansand', 'Oslo']
\`\`\`

The quotation marks show that the values are text.

## An empty list

A list can also start with no contents:

\`\`\`python
measurements = []

print(measurements)
\`\`\`

Result:

\`\`\`text
[]
\`\`\`

This is called an **empty list**.

Later, we will learn how to add values to it.

## A list has an order

In this list:

\`\`\`python
days = ["Monday", "Tuesday", "Wednesday"]
\`\`\`

\`Monday\` comes first, \`Tuesday\` next, and \`Wednesday\` last.

The order is part of the list.

In the next lesson, we will learn how to retrieve one particular value from that order.

## Use the list with what you already know

You learned \`for\` in M5.

A \`for\` loop works very well with a list:

\`\`\`python
temperatures = [18, 20, 17, 21]

for temperature in temperatures:
    print("Temperature:", temperature)
\`\`\`

Result:

\`\`\`text
Temperature: 18
Temperature: 20
Temperature: 17
Temperature: 21
\`\`\`

We no longer need one variable and one \`print()\` for each reading.

## Follow the loop

The first time through the loop:

\`\`\`text
temperature = 18
\`\`\`

The next time:

\`\`\`text
temperature = 20
\`\`\`

Then 17 and 21.

The list keeps all the values. The loop variable \`temperature\` receives one of them at a time.

## Why are lists useful?

Lists are useful when we have several related values, for example:

- temperature readings
- names
- prices
- electricity use per day
- file names
- appointments or tasks

We do not need to know in advance everything we will later do with the values. First, we learn to collect them neatly.

## Change it

Start with:

\`\`\`python
temperatures = [18, 20, 17, 21]
\`\`\`

Change some of the values.

Add a fifth value inside the square brackets.

Run the program again.

## Make it yourself

Create a list with at least four related values.

First print the whole list.

Then use a \`for\` loop to print one value at a time.

## What you learned

You can now:

- explain why a list can be better than many separate variables
- create a list with \`[\` and \`]\`
- create lists containing numbers or text
- create an empty list
- explain that a list has an order
- print the whole list
- go through a list with \`for\`

The next lesson is about retrieving one particular value from a list.
