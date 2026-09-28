# M3.2 – Turn input into numbers

`input()` always returns text. To calculate with what the user enters, we first need to convert that text into a number.

## Why do we need conversion?

This does not work:

```python
age = input("Age: ")
print(age + 1)
```

If you enter `70`, `age` contains the text `"70"`.

Python cannot add the number `1` to a string.

## Integers with int()

`int()` can turn text representing a whole number into a Python integer:

```python
age_text = input("Age: ")
age = int(age_text)

print("Next year:")
print(age + 1)
```

You can also write it more compactly:

```python
age = int(input("Age: "))
print(age + 1)
```

The first version makes the individual steps more visible. Both are valid Python.

## Decimal numbers with float()

For values that may contain decimals, we often use `float()`:

```python
price = float(input("Price per kWh: "))
consumption = float(input("Consumption in kWh: "))

cost = price * consumption

print("Cost:")
print(cost)
```

When entering decimal values for Python, use a decimal point, for example `1.25`, rather than `1,25`.

## Try it

Run the program above with:

```text
Price per kWh: 1.25
Consumption in kWh: 6
```

Python can now calculate with both answers because they have been converted to numbers.

## int or float?

Use `int()` when you want a whole number, for example:

```python
quantity = int(input("Quantity: "))
```

Use `float()` when the value may contain decimals:

```python
temperature = float(input("Temperature: "))
```

`float()` can also read text such as `"6"`; the result is the floating-point number `6.0`.

## When the text cannot become a number

Try:

```python
quantity = int(input("Quantity: "))
```

and enter:

```text
six
```

Python reports an error similar to:

```text
ValueError: invalid literal for int() with base 10: 'six'
```

Here, **ValueError** means Python received a value, but that value could not be used as the operation required.

`int()` knows how to turn the text `"6"` into a number. It does not know how to convert the word `"six"`.

## Read the error

When you see `ValueError` around numeric input:

1. see which conversion was used – `int()` or `float()`
2. look at what the user entered
3. check whether the text really has a valid numeric format

Later, you will learn how a program can handle invalid input itself. For now, the goal is to understand why the error occurs.

## Change it

Create a program that asks for quantity and price:

```python
quantity = int(input("Quantity: "))
price = float(input("Price per item: "))

total = quantity * price

print("Total:")
print(total)
```

Try several valid values.

Then deliberately enter an invalid value and read the error message.

## Make it yourself

Create a program that:

- asks the user for at least two numbers
- uses `int()` or `float()` appropriately
- calculates a result
- stores the result in a variable
- prints explanatory text and the result

## What you learned

You can now:

- explain why `input()` needs conversion before numeric calculations
- use `int()`
- use `float()`
- choose between whole and decimal numbers
- recognize and begin to understand `ValueError`

The next lesson combines these ideas into a complete small interactive program.
