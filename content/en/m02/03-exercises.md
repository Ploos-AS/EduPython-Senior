# M2.3 – Exercises and debugging

Try each exercise yourself before reading the guidance or solution.

## Exercise 1 – Name the values

Rewrite:

```python
print(12 * 4.50)
```

so both numbers are first stored in clearly named variables.

### Possible solution

```python
quantity = 12
price_per_item = 4.50
print(quantity * price_per_item)
```

## Exercise 2 – Store the result

Extend the program so the result also has a name.

### Possible solution

```python
quantity = 12
price_per_item = 4.50
total = quantity * price_per_item

print("Total:")
print(total)
```

## Exercise 3 – What gets printed?

Predict the result before running:

```python
number = 5
double = number * 2
number = 8

print(number)
print(double)
```

### Solution

The program prints:

```text
8
10
```

`double` received the value `10` when that line ran. It is not automatically recalculated when `number` later becomes `8`.

## Exercise 4 – Find the NameError

What is wrong?

```python
price = 25
quantity = 3
total = price * quantity

print(totall)
```

### Guidance

Compare the name that receives the result with the name used in `print()`.

### Solution

The variable is called `total`, but the program tries to use `totall`.

```python
print(total)
```

Variable names must be written consistently.

## Exercise 5 – Better names

This code works:

```python
a = 120
b = 3
c = a / b
print(c)
```

Rewrite it with names explaining that 120 kilometres are to be divided across 3 days.

### Possible solution

```python
distance_km = 120
number_of_days = 3
km_per_day = distance_km / number_of_days

print(km_per_day)
```

## Exercise 6 – Intermediate results

Create a program with:

```text
power = 1500 watts
time = 2 hours
price = 1.25 per kWh
```

Calculate kilowatts first, then kWh, then the cost. Use a variable for each step.

### Possible solution

```python
power_watts = 1500
hours = 2
price_per_kwh = 1.25

power_kw = power_watts / 1000
consumption_kwh = power_kw * hours
cost = consumption_kwh * price_per_kwh

print(cost)
```

## Mini-project

Create a program that calculates something useful or interesting to you.

Requirements:

- at least three starting variables
- clear variable names
- at least one intermediate result
- a final result stored in a variable
- explanatory output
- change at least one starting value and check that the new result makes sense

Examples include costs, distances, quantities, time, or another simple calculation.

## Before moving on

You are ready for M3 when you can explain:

- why a variable is useful
- what `=` does in Python
- why good names help
- why an earlier calculated result does not change automatically
- what you should check first when you see `NameError`

In M3, the program will stop being completely fixed: the user will be able to enter values while the program is running.
