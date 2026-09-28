# M5.6 – A practical program with several measurements

Now we combine loops, input, decisions, and a result that is built over several iterations.

We will create a small electricity-use program.

## The goal

The program will ask for electricity use for three days.

For each day, it will:

- read the usage
- add it to the total
- give a simple message if the usage is high

Finally, it will print the total usage.

## Try it

```python
total_kwh = 0

for day in range(1, 4):
    print("Day", day)
    kwh = float(input("Usage in kWh: "))

    total_kwh = total_kwh + kwh

    if kwh > 20:
        print("Usage was above 20 kWh on this day.")
    else:
        print("Usage was 20 kWh or lower on this day.")

print("Total usage:", total_kwh, "kWh")
```

## See the structure

Before the loop:

```python
total_kwh = 0
```

This creates the result that will be built up.

The loop:

```python
for day in range(1, 4):
```

gives three iterations: 1, 2, and 3.

On each iteration, one measurement is read:

```python
kwh = float(input("Usage in kWh: "))
```

Then it is added to the total:

```python
total_kwh = total_kwh + kwh
```

The `if` then evaluates that particular measurement.

After the loop, the final result is printed once.

## Follow an example

Suppose the user enters:

```text
10
25
15
```

The total develops like this:

```text
start: 0
day 1: 0 + 10 = 10
day 2: 10 + 25 = 35
day 3: 35 + 15 = 50
```

Only day 2 produces the message about usage above 20 kWh.

The final result is 50 kWh.

## Why is input inside the loop?

We need a new measurement for every day.

If `input()` were before the loop, the program would read only one value and use the same value several times.

The position of an instruction determines **when** and **how often** it runs.

## Why is the total outside?

If we wrote:

```python
for day in range(1, 4):
    total_kwh = 0
```

the total would be reset for every day.

The starting value must be created once before the loop.

## Test systematically

Try, among other cases:

- all measurements below 20
- one measurement exactly 20
- one measurement above 20
- decimal values such as 12.5

Predict both the messages and the total before running the program.

## Change it

Change the program to five days.

Which part needs to change?

Also change the threshold for “high usage” from 20 to another value.

## Make it yourself

Create a program that processes several measurements.

It should:

- use `for`
- read a new numeric value on every iteration
- build a total or counter
- use `if` on every measurement
- print a final result after the loop

Possible themes include costs, kilometres, minutes, scores, or other measurements.

## What you learned

You can now combine:

**starting value → loop → input → update → decision → final result**

You can also explain why some instructions must be before, inside, or after the loop.

The next section brings all of M5 together with exercises and debugging.
