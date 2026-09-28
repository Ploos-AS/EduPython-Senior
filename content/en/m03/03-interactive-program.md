# M3.3 – A complete interactive program

Now we combine what you have learned about variables, `input()`, `float()`, and calculations.

We will build a simple energy-cost calculator.

## Try it

```python
consumption_text = input("Consumption in kWh: ")
price_text = input("Price per kWh: ")

consumption = float(consumption_text)
price = float(price_text)

cost = consumption * price

print("Calculated cost:")
print(cost)
```

The program follows a clear sequence:

1. ask the user
2. store the text answers
3. convert the text to numbers
4. perform the calculation
5. print the result

It is a small program, but it follows the same basic idea as much larger programs: **data in → processing → result out**.

## Why keep the text variables?

We could write:

```python
consumption = float(input("Consumption in kWh: "))
```

That is shorter. For now, however, the longer version is useful because you can see every step.

As you gain experience, you can choose whichever form is clearest.

## Change it

Extend the program with a number of days:

```python
consumption_per_day = float(input("Consumption per day in kWh: "))
number_of_days = int(input("Number of days: "))
price = float(input("Price per kWh: "))

total_consumption = consumption_per_day * number_of_days
cost = total_consumption * price

print("Total consumption:")
print(total_consumption)
print("Calculated cost:")
print(cost)
```

Notice that `number_of_days` uses `int()`, while values that may contain decimals use `float()`.

## What happens with invalid input?

If the program expects a number and the user enters a word, Python may stop with `ValueError`.

For now, that is expected behavior. The goal in M3 is to understand input and conversion.

Later, you will learn how programs make decisions and handle more situations themselves.

## Make it yourself

Choose one small calculator, for example:

- price × quantity
- kilometres per day × number of days
- hours × price per hour
- temperature conversion
- simple interest for one year

The program should:

- ask for at least two values
- use clear variable names
- convert input to the appropriate numeric type
- store at least one intermediate or final result in a variable
- print explanatory text with the result

Run the program several times with different values.

## Think through the program

Before moving on, you should be able to point out:

- where data enters
- where text becomes numbers
- where the calculation happens
- where the result comes out

This pattern will appear throughout the rest of the course.
