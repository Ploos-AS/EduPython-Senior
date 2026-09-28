# M6.5 – A small program with several functions

Functions are most useful when they make a program easier to understand.

Now we will create a small program that calculates the cost of a trip.

We will divide the work into small functions.

## Try it

\`\`\`python
def calculate_cost(kilometres, price_per_km):
    return kilometres * price_per_km


def show_result(kilometres, cost):
    print("Distance:", kilometres, "km")
    print("Cost:", cost)


kilometres = 120
price_per_km = 1.50

cost = calculate_cost(kilometres, price_per_km)
show_result(kilometres, cost)
\`\`\`

The program has two clear jobs:

- \`calculate_cost()\` performs the calculation
- \`show_result()\` displays the result

## Follow the data

Start:

\`\`\`text
kilometres = 120
price_per_km = 1.50
\`\`\`

Then:

\`\`\`python
cost = calculate_cost(kilometres, price_per_km)
\`\`\`

The function calculates:

\`\`\`text
120 × 1.50 = 180
\`\`\`

and returns 180.

The variable \`cost\` therefore receives 180.

Finally, we pass the values to:

\`\`\`python
show_result(kilometres, cost)
\`\`\`

## Why divide a program into functions?

We could write everything in one long block.

But functions let us give parts of the program names:

**calculate** and **show**.

That makes the program easier to read.

If the calculation needs changing, we know where to look.

## A function should have a clear job

Compare:

\`\`\`python
def calculate_cost(kilometres, price_per_km):
    return kilometres * price_per_km
\`\`\`

with a function that:

- asks the user for many things
- performs several unrelated calculations
- prints many messages
- stores data
- and ends the program

The first is easier to understand because its job is clear.

## Functions can be reused

\`\`\`python
cost1 = calculate_cost(50, 1.50)
cost2 = calculate_cost(200, 1.50)

print(cost1)
print(cost2)
\`\`\`

The same calculation can be used with different values.

## Functions can work together

We will return to this later, but you can already see the pattern:

\`\`\`python
cost = calculate_cost(kilometres, price_per_km)
show_result(kilometres, cost)
\`\`\`

One function produces a result that another function uses.

## Change it

Change:

\`\`\`python
kilometres = 120
\`\`\`

to a different distance.

Also change \`price_per_km\`.

Predict the cost before running the program.

## Make it yourself

Create a small program with at least two functions.

One function should:

- receive values
- calculate something
- return the result

The other should:

- receive a result
- display it clearly

Use both functions from the main part of the program.

## What you learned

You can now:

- divide a program into functions
- give each function a clear responsibility
- send data from the main program into a function
- return data from a function
- pass a returned result to another function
- reuse functions with different values

The next lesson shows how functions can make code easier to test and debug.
