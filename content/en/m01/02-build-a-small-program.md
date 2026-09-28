# M1.2 – Build a small program

Now you will combine what you already know into a small program.

We use electricity consumption as an example, but the important part is the Python code. You can later replace the example with something that interests you.

## Try it

An appliance uses 1000 watts for 3 hours. That equals 3 kilowatt-hours (kWh).

If one kWh costs 1.20, Python can calculate the energy cost:

```python
print("A simple energy calculation")
print("Consumption in kWh:")
print(3)
print("Cost:")
print(3 * 1.20)
```

Run the program and inspect the result.

Python distinguishes the text that explains the result from the numbers it calculates with.

## Let Python do more of the calculation

We can write the calculation directly:

```python
print("Three hours at 1000 watts gives:")
print(1000 / 1000 * 3)
print("kWh")
```

Python follows the usual rules of arithmetic.

Parentheses can make the intention clearer:

```python
print((1000 / 1000) * 3)
```

Both expressions produce the same result.

## Change it

Try changing the numbers.

What does 5 kWh cost when the price is 1.50 per kWh?

```python
print(5 * 1.50)
```

What is the result for 8 kWh at 0.90?

Write the expression yourself before running the program.

## A program can explain its result

A useful program does not just display a lonely number.

Compare:

```python
print(7.5)
```

with:

```python
print("Calculated cost:")
print(5 * 1.50)
```

The second version is easier to understand when you open the program again later.

## Another error to recognize

Try:

```python
print(10 / 0)
```

Python responds with an error message ending in:

```text
ZeroDivisionError: division by zero
```

This is not a syntax error. Python understands the instruction, but the calculation itself cannot be performed.

It is useful to distinguish:

- **SyntaxError** – Python cannot interpret how the code is written.
- **ZeroDivisionError** – the code is valid Python, but the operation cannot be performed.

The error type near the bottom of the message is often a good place to start.

## Make it yourself

Create a program that works like a small calculator report.

The program should:

1. print a heading
2. explain what is being calculated
3. perform at least three different calculations
4. print text that makes the results understandable

You can use electricity, travel distances, recipes, temperatures, or something completely different.

Do not use variables yet. They arrive in the next milestone.

## Challenge

Can you predict the result before running this?

```python
print(10 + 2 * 3)
print((10 + 2) * 3)
```

Then run the program and compare.

Parentheses can change the order of calculation, just as in ordinary mathematics.

## What you learned

You have now used several Python instructions together to make a small program. You can combine explanatory text with calculations, and you have encountered two different kinds of errors.

In M2, programs become much more flexible when we store values in **variables**.
