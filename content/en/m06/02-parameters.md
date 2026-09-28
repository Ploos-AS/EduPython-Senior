# M6.2 – Give a function information with parameters

A function becomes even more useful when it can receive information from outside.

This information is called a **parameter**.

## Try it

\`\`\`python
def say_hello(name):
    print("Hello,", name)

say_hello("Anna")
say_hello("Bjørn")
\`\`\`

The same function can be used with different names.

## What is the parameter?

In:

\`\`\`python
def say_hello(name):
\`\`\`

\`name\` is the parameter.

When we write:

\`\`\`python
say_hello("Anna")
\`\`\`

\`"Anna"\` is the value we pass to the function.

You can think of it this way:

**parameter = place for information**

**argument = information actually passed in**

We can simply say “value” when we want to keep the explanation easy.

## Multiple parameters

A function can receive several values:

\`\`\`python
def show_person(name, age):
    print(name, "is", age, "years old.")

show_person("Anna", 72)
show_person("Bjørn", 68)
\`\`\`

Order matters.

\`name\` receives the first value, and \`age\` receives the second.

## Follow the values

When we write:

\`\`\`python
show_person("Anna", 72)
\`\`\`

you can read it as:

- \`name\` becomes \`"Anna"\`
- \`age\` becomes \`72\`
- the function runs with those values

The next call can use completely different values.

## The function can calculate

\`\`\`python
def show_double(number):
    doubled = number * 2
    print("Double:", doubled)

show_double(5)
show_double(12)
\`\`\`

A parameter can be used just like an ordinary variable inside the function.

## A common error

If a function needs one parameter:

\`\`\`python
def say_hello(name):
    print("Hello,", name)
\`\`\`

we must provide a value:

\`\`\`python
say_hello("Anna")
\`\`\`

A call without a value:

\`\`\`python
say_hello()
\`\`\`

causes an error because the function is missing required information.

## Parameters make functions reusable

Without a parameter we could write:

\`\`\`python
def say_hello_anna():
    print("Hello, Anna")
\`\`\`

But that function is tied to one name.

With a parameter:

\`\`\`python
def say_hello(name):
    print("Hello,", name)
\`\`\`

it can be used with many names.

## Change it

Create a function with one parameter.

Try passing:

- text
- another piece of text
- a number

Make sure the operation inside the function matches the type of value you pass.

## Make it yourself

Create a function that:

- has at least one parameter
- uses the parameter inside the function
- is called at least three times
- receives different values in the calls

A function that calculates or displays something practical is a good choice.

## What you learned

You can now:

- define a function with a parameter
- pass a value to a function
- use the parameter inside the function
- use multiple parameters
- explain why argument order matters
- create more reusable functions

The next lesson is about return values: when a function gives a result back to the rest of the program.
