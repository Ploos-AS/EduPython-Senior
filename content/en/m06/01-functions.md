# M6.1 – Give a group of instructions a name

We have now built programs with variables, decisions, and loops.

As programs grow, it can be useful to group instructions that belong together.

A **function** is a named group of instructions that can be used when needed.

## Try it

\`\`\`python
def show_welcome():
    print("Welcome!")
    print("This is EduPython-Senior.")

show_welcome()
show_welcome()
\`\`\`

The function is defined with \`def\`, but the instructions run only when we **call** \`show_welcome()\`.

It is important to distinguish:

\`\`\`python
def show_welcome():
\`\`\`

which defines the function, from:

\`\`\`python
show_welcome()
\`\`\`

which asks Python to run it.

## Indentation

As with \`if\` and loops, indentation shows which lines belong to the function:

\`\`\`python
def say_hello():
    print("Hello!")
    print("Have a nice day.")

print("The program starts")
say_hello()
print("The program continues")
\`\`\`

The two \`print()\` lines in the function run when the function is called.

## A common misunderstanding

This:

\`\`\`python
def show_message():
    print("Hello!")
\`\`\`

does not necessarily print \`Hello!\` when the program starts. The function has only been defined.

This calls it:

\`\`\`python
show_message()
\`\`\`

## Why is this useful?

If the same work is needed in several places, we write the instructions once:

\`\`\`python
def show_message():
    print("Remember to save your work.")
\`\`\`

Then we can use:

\`\`\`python
show_message()
\`\`\`

in several places.

If the message needs changing, we change it in one place.

## Change it

Create a function that prints a short message of your choice.

Call it once, and then three times.

## Make it yourself

Create a function that:

- has a clear name
- contains at least two instructions
- is called at least twice

Also write some code outside the function so the difference is clear.

## What you learned

You can now:

- explain what a function is
- define a simple function with \`def\`
- call a function
- explain the difference between defining and calling
- use indentation to show the function block
- reuse the same function several times

The next lesson gives the function information through parameters.
