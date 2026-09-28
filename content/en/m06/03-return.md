# M6.3 – Return a result with return

A function can display something with \`print()\`. But often we want the function to **give a result back** so the rest of the program can use it.

For that, we use \`return\`.

## First with print

\`\`\`python
def show_double(number):
    print(number * 2)

show_double(5)
\`\`\`

This displays the result.

But what if we want to store the result?

## Use return

\`\`\`python
def calculate_double(number):
    return number * 2

result = calculate_double(5)

print("Result:", result)
\`\`\`

The function calculates \`10\` and **returns** the value to the place where the function was called.

## print and return are not the same

This:

\`\`\`python
def with_print(number):
    print(number * 2)
\`\`\`

displays a result.

This:

\`\`\`python
def with_return(number):
    return number * 2
\`\`\`

gives the result back.

A function with \`return\` does not have to display anything.

## Use the result again

When a function returns a value, we can use it like an ordinary value:

\`\`\`python
def calculate_double(number):
    return number * 2

result = calculate_double(5)
new_value = result + 3

print(new_value)
\`\`\`

The result is 10, followed by 13 after the second calculation.

## return ends the function

When Python reaches \`return\`, it leaves the function immediately.

\`\`\`python
def test():
    print("Before")
    return 10
    print("After")
\`\`\`

\`After\` is never printed.

This is useful when the function has found the result it should return.

## Multiple return points come later

A function can have multiple \`return\` statements, often together with \`if\`.

We will wait with those examples until decisions inside functions are well established.

## Practical example

\`\`\`python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(25, 4)

print("Total:", total)
\`\`\`

The function does not need to know anything about the rest of the program. It performs one calculation and returns the result.

This makes it easy to test and reuse.

## A function returning text

\`\`\`python
def make_greeting(name):
    return "Hello, " + name + "!"

message = make_greeting("Anna")
print(message)
\`\`\`

\`return\` can return text, not only numbers.

## Change it

Create a function that accepts a value and returns a calculated result.

Store the result in a variable.

Then use that variable in another calculation or print it.

## Make it yourself

Create a function that:

- has at least one parameter
- uses the parameter in a calculation
- uses \`return\`
- is called at least twice
- stores at least one returned result in a variable

## What you learned

You can now:

- explain what \`return\` does
- distinguish \`print()\` from \`return\`
- store a returned value
- use the result elsewhere in the program
- explain that \`return\` ends the function
- create functions that return numbers and text

The next lesson combines functions with \`if\` and \`for\`.
