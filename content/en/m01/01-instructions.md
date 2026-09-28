# M1.1 – Giving the computer instructions

A program is a series of instructions. Python reads the instructions and executes them in the order in which they appear.

We begin with `print()`. It tells Python to display something on the screen.

## Try it

Type:

```python
print("Hello!")
```

Run the program. You should see:

```text
Hello!
```

The text between the quotation marks is a **string**.

Try several instructions:

```python
print("Good morning")
print("I am learning Python")
print("One instruction at a time")
```

Python executes them from top to bottom.

## Change it

Replace the text with something of your own:

```python
print("My first Python text")
```

Then add another line. What happens if you reverse the order of the two `print()` lines?

## Numbers are not text

Python can also print numbers:

```python
print(42)
print(3.14)
```

Numbers do not need quotation marks.

This becomes important because Python can **calculate** with numbers:

```python
print(2 + 3)
print(10 - 4)
print(6 * 7)
print(20 / 4)
```

Python displays the result of each expression.

## Text or calculation?

Compare:

```python
print(2 + 3)
print("2 + 3")
```

The first line displays `5`. The second displays the text `2 + 3`.

Quotation marks tell Python to treat the contents as text.

## When Python reports an error

Errors are a normal part of programming. Python tries to tell you where the problem is.

Try this deliberately:

```python
print("Hello!)
```

You will get an error message containing `SyntaxError`.

**Syntax** means the rules for how Python code must be written. Here, the closing quotation mark is missing.

Correct the line:

```python
print("Hello!")
```

When you encounter an error message:

1. look at the line Python points to
2. read the name of the error
3. inspect the code near the place Python marks
4. change one thing and try again

You do not need to understand the entire error message immediately.

## Make it yourself

Create a small program that prints:

- a heading
- two lines of text
- the result of at least two calculations

Use at least one of the operators `+`, `-`, `*`, and `/`.

Run the program and check that the results are what you expected.

## What you learned

You can now:

- give Python a simple instruction
- use `print()`
- print text and numbers
- use Python as a simple calculator
- distinguish text from a mathematical expression
- recognize `SyntaxError` and begin reading an error message

Next, you will give values names by using **variables**.
