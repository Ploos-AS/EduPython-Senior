# M5.5 – Repeat while something is true with while

A `for` loop works well when a program needs to visit a known sequence.

Sometimes, instead, we know that the program should continue **while a condition is true**.

For that, we can use `while`.

## Try it

```python
number = 1

while number <= 5:
    print(number)
    number = number + 1

print("Finished")
```

The program prints the numbers 1 through 5.

## Read while as a sentence

This line:

```python
while number <= 5:
```

can be read:

**While number is less than or equal to 5, do this.**

Before every iteration, Python tests the condition again.

## Three important parts

This kind of `while` loop has three parts.

### 1. Starting value

```python
number = 1
```

### 2. Condition

```python
while number <= 5:
```

### 3. Update

```python
number = number + 1
```

The update eventually makes the condition false.

## Follow the program

First test:

```text
1 <= 5 → true
```

The program prints 1 and changes `number` to 2.

Later:

```text
5 <= 5 → true
```

The program prints 5 and changes `number` to 6.

Next test:

```text
6 <= 5 → false
```

The loop stops.

## An infinite loop

Look at:

```python
number = 1

while number <= 5:
    print(number)
```

What changes `number`?

Nothing.

The value remains 1, and `1 <= 5` keeps being true. The loop therefore does not stop by itself.

This is called an **infinite loop**.

If a program appears to keep running without finishing, a loop that never reaches its stopping condition is one of the first things to investigate.

## while can also stop because of input

```python
answer = input("Enter yes to continue: ")

while answer == "yes":
    print("You chose to continue.")
    answer = input("Enter yes to continue: ")

print("Finished")
```

Here, we do not know in advance how many iterations the loop will run.

The condition is tested again after every answer.

## Why is input read before and inside the loop?

The program needs a first answer before it can test:

```python
while answer == "yes":
```

Inside the loop, we read a new answer so the condition can change.

If the second `input()` line is missing, an initial answer of `yes` makes the loop continue without asking again.

## for or while?

At this stage, you can use this rule of thumb:

- use `for` when visiting a known sequence or a known number of iterations
- use `while` when repetition is controlled by a condition that can change

There are more possibilities later, but this is a good starting point.

## Change it

Change:

```python
number = 1
while number <= 5:
```

so the loop prints different starting and ending values.

Predict the final value that will be printed.

## Make it yourself

Create a safe `while` loop that:

- has a starting value
- has a clear condition
- changes a value inside the loop
- eventually makes the condition false
- prints a message after the loop has finished

Before running it, explain to yourself **why the loop will stop**.

## What you learned

You can now:

- explain what a `while` loop does
- read a `while` condition
- identify the starting value, condition, and update
- explain why a loop can become infinite
- use input to control how long a loop continues
- choose between a simple `for` and `while` loop

The next section uses loops in a complete practical program.
