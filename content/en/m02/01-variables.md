# M2.1 – Give values names

In M1, we wrote numbers and text directly inside instructions. That works, but a program quickly becomes difficult to change when the same value is used in several places.

A **variable** gives a value a name.

## Why use variables?

Compare:

```python
print(5 * 1.50)
```

with:

```python
quantity = 5
price = 1.50
print(quantity * price)
```

Both calculate the same thing. The second version tells us what the numbers mean.

## Try it

Type:

```python
name = "Ada"
age = 70

print(name)
print(age)
```

Python stores the text `"Ada"` under the name `name`, and the number `70` under the name `age`.

When `print(name)` runs, Python finds the value referred to by the variable `name`.

## What does = mean?

In Python:

```python
price = 1.50
```

roughly means “let `price` have the value `1.50`.”

This is called **assignment**.

It is not quite the same as the equals sign in mathematics. Python uses `=` to assign a value to a name.

## Use variables in calculations

```python
consumption = 5
price_per_kwh = 1.50

print("Cost:")
print(consumption * price_per_kwh)
```

Now you can change `consumption` or `price_per_kwh` in one place and run the program again.

## Change it

Try:

```python
consumption = 8
price_per_kwh = 0.90

print(consumption * price_per_kwh)
```

Change the values and see how the result changes.

## A variable can receive a new value

```python
temperature = 18
print(temperature)

temperature = 21
print(temperature)
```

The second assignment means that `temperature` now refers to `21`.

This is an important difference from how letters are often used in mathematics.

## Good names help you

This works:

```python
x = 5
y = 1.50
print(x * y)
```

But this is easier to understand:

```python
quantity = 5
price = 1.50
print(quantity * price)
```

Choose names that describe what the value means.

Variable names can contain letters, numbers, and underscores, among other characters, but cannot begin with a number.

```python
price_per_kwh = 1.50
```

is a common, clear Python name.

## When Python does not know the name

Deliberately try:

```python
print(cost)
```

without first creating a variable called `cost`.

Python will report:

```text
NameError: name 'cost' is not defined
```

Here, **NameError** means Python cannot find the name you asked it to use.

Check:

1. Was the variable given a value before it was used?
2. Is the name spelled exactly the same in both places?
3. Did you mistype a letter?

## Make it yourself

Create a program with at least three variables:

- one containing text
- one containing an integer
- one containing a decimal number

Print the variables and use at least two numeric variables in a calculation.

Then change one value and run the program again.

## What you learned

You can now:

- explain why variables are useful
- assign values with `=`
- use variables in `print()` and calculations
- change the value of a variable
- choose clear variable names
- recognize a simple `NameError`

The next lesson uses variables to build a more practical program.
