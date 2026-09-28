# M2.2 – A program that is easy to change

In M1, we wrote numbers directly inside calculations. Variables can now make the program clearer and easier to change.

## From expression to program

This works:

```python
print(5 * 1.50)
```

But what do `5` and `1.50` mean?

Variables make the intention clear:

```python
consumption_kwh = 5
price_per_kwh = 1.50

print(consumption_kwh * price_per_kwh)
```

## Give the result a name too

A result can be stored in another variable:

```python
consumption_kwh = 5
price_per_kwh = 1.50
cost = consumption_kwh * price_per_kwh

print("Calculated cost:")
print(cost)
```

Read this line:

```python
cost = consumption_kwh * price_per_kwh
```

from right to left:

1. Python finds the values of `consumption_kwh` and `price_per_kwh`.
2. Python multiplies them.
3. The result is assigned to the name `cost`.

## Try it

Create and run the program above.

Then change only:

```python
consumption_kwh = 8
```

Run the program again. The rest of the program does not need to change.

That is an important reason for using variables.

## Intermediate results

We can split a calculation into understandable steps:

```python
power_watts = 1000
hours = 3
price_per_kwh = 1.20

power_kw = power_watts / 1000
consumption_kwh = power_kw * hours
cost = consumption_kwh * price_per_kwh

print("Consumption in kWh:")
print(consumption_kwh)
print("Cost:")
print(cost)
```

The program is longer than one large expression, but each step has a name.

That makes the code easier to read, check, and change.

## Change it

Try:

```python
power_watts = 750
hours = 4
price_per_kwh = 1.10
```

Before running the program, try to estimate the result.

## A value is calculated when the line runs

Look closely at this:

```python
price = 10
double_price = price * 2

price = 20

print(double_price)
```

The program prints `20`, not `40`.

When `double_price = price * 2` ran, `price` was `10`. The result `20` was stored in `double_price`.

Changing `price` later does not automatically recalculate earlier lines.

## Make it yourself

Create a small program that calculates a total from at least three named values.

For example, you could use:

- quantity and price
- distance and cost per kilometre
- number of portions and amount per portion
- hours and a value per hour

Requirements:

1. use clear variable names
2. create at least one intermediate result
3. store the final result in a variable
4. print explanatory text and the result
5. change one starting value and run the program again

## What you learned

You can now use variables for starting values, intermediate results, and final results. You have also seen that Python performs assignments when execution reaches them — earlier calculations are not automatically updated.

The next section gives you more practice before we move on to interactive programs.
