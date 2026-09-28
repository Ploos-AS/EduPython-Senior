# M4.4 – Combine conditions

Some decisions depend on more than one question. Python provides the words `and`, `or`, and `not` to combine or reverse conditions.

## and – both must be true

```python
temperature = float(input("Temperature: "))

if temperature >= 0 and temperature < 20:
    print("The temperature is from 0 to below 20.")
```

The complete condition is true only when **both** parts are true.

For `10`:

- `temperature >= 0` is true
- `temperature < 20` is true
- the complete expression is therefore true

For `25`, the second part is false, so the block does not run.

## or – at least one must be true

```python
temperature = float(input("Temperature: "))

if temperature < 0 or temperature > 30:
    print("The temperature is outside the range 0 to 30.")
```

Here, it is enough for **at least one** part to be true.

## not – reverse true and false

`not` reverses the result of a condition.

```python
is_ready = input("Enter yes when you are ready: ") == "yes"

if not is_ready:
    print("You did not enter yes.")
```

If `is_ready` is false, `not` makes the expression true.

This example compares the text exactly. `"Yes"` and `"yes"` are different strings.

## Read the expression as a sentence

This code:

```python
if age >= 18 and age <= 100:
```

can be read as:

**If age is at least 18 and age is at most 100.**

If an expression becomes difficult to read, it is often better to make the program clearer rather than force everything onto one line.

## Parentheses can make intent clearer

You can write:

```python
if (temperature < 0) or (temperature > 30):
    print("Outside the range")
```

The parentheses are not required in this simple expression, but they can make the two parts easier to see.

For now, we keep combinations simple.

## Change it

Try:

```python
number = int(input("Number: "))

if number >= 10 and number <= 20:
    print("The number is from 10 through 20.")
else:
    print("The number is outside the range.")
```

Test `9`, `10`, `15`, `20`, and `21`.

## A common mistake with and

This is not the correct way to write “between 10 and 20”:

```python
if number >= 10 and <= 20:
```

Each comparison must be complete:

```python
if number >= 10 and number <= 20:
```

Later, you may encounter other valid Python ways to express ranges. Here, we use the form that shows both questions clearly.

## Make it yourself

Create a program that uses at least one of:

- `and`
- `or`
- `not`

Test several values and explain to yourself why the complete condition becomes true or false.

## What you learned

You can now:

- use `and` when both conditions must be true
- use `or` when at least one must be true
- use `not` to reverse a true-or-false result
- read a combined condition as a sentence
- keep logical expressions simple and readable

The next section uses decisions in a complete practical program.
