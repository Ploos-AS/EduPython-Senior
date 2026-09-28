# M6.4 – Functions together with if and for

We can now combine functions with decisions and loops.

This is an important step: a function can receive values, work with them, and return a result.

## Try it – function with if

\`\`\`python
def temperature_message(temperature):
    if temperature < 0:
        return "Below zero"
    elif temperature < 20:
        return "From 0 to below 20"
    else:
        return "20 or above"

print(temperature_message(-5))
print(temperature_message(12))
print(temperature_message(25))
\`\`\`

The function receives one value and chooses the appropriate result.

Notice that we do not need three separate temperature programs. The function can be used with many values.

## Follow one call

When we write:

\`\`\`python
temperature_message(12)
\`\`\`

the parameter becomes:

\`\`\`text
temperature = 12
\`\`\`

Python tests the first condition:

\`\`\`text
12 < 0
\`\`\`

It is false.

Then it tests:

\`\`\`text
12 < 20
\`\`\`

It is true.

The function returns:

\`\`\`text
"From 0 to below 20"
\`\`\`

## A function inside a for loop

The function can also be used for every value in a loop:

\`\`\`python
def temperature_message(temperature):
    if temperature < 0:
        return "Below zero"
    elif temperature < 20:
        return "From 0 to below 20"
    else:
        return "20 or above"

temperatures = [-5, 4, 18, 23]

for temperature in temperatures:
    message = temperature_message(temperature)
    print(temperature, ":", message)
\`\`\`

The same work happens several times, but the decision logic lives in one place.

## Why is this useful?

Without the function, we could copy the whole \`if\` structure every time.

With the function we have:

**one rule → many users of the rule**

If the rule changes, we change it in one place.

## A function can use a loop

It can also work the other way:

\`\`\`python
def sum_numbers(start, stop):
    total = 0

    for number in range(start, stop):
        total = total + number

    return total

print(sum_numbers(1, 6))
\`\`\`

Here, the \`for\` loop is inside the function.

The function adds 1 through 5 and returns the result.

## Follow the data flow

When we write:

\`\`\`python
sum_numbers(1, 6)
\`\`\`

we can follow:

1. \`start\` becomes 1
2. \`stop\` becomes 6
3. \`total\` starts at 0
4. the loop visits 1, 2, 3, 4, and 5
5. \`total\` is built up
6. the function returns 15

## Do not make functions unnecessarily large

A function should preferably have a clear job.

This is easy to understand:

\`\`\`python
def calculate_total(price, quantity):
    return price * quantity
\`\`\`

A function that reads many inputs, prints long messages, makes many decisions, and calculates several unrelated things can become harder to understand.

We will learn more about this later.

## Change it

Change the temperature function so its boundaries fit your own categories.

Test several values.

Also change the list of temperatures without changing the function itself.

## Make it yourself

Create a function that:

- has at least one parameter
- uses \`if\` or \`elif\`
- returns a result
- is called from a \`for\` loop

Or create a function that contains a \`for\` loop and returns a combined result.

## What you learned

You can now:

- use \`if\` inside a function
- use \`for\` inside a function
- call a function from a loop
- return different results from decisions
- follow data from parameter to result
- reuse one rule for many values

The next lesson shows how functions can make a complete small program more organised.
