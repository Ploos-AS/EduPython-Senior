# M5.1 – Do something several times with for

Programs often need to do the same kind of work several times.

We could copy the same instruction:

```python
print("Anna")
print("Bjørn")
print("Cecilie")
```

But with many values, that copying becomes cumbersome. A **loop** lets the program repeat a block of code.

## Try it

```python
names = ["Anna", "Bjørn", "Cecilie"]

for name in names:
    print(name)

print("Finished")
```

The result is:

```text
Anna
Bjørn
Cecilie
Finished
```

You do not need to understand every detail of the square brackets yet. For now, read the first line as “here are three values.”

## Read for as a sentence

This line:

```python
for name in names:
```

can be read:

**For each name in names, do this.**

Python takes one value at a time and temporarily stores it in the variable `name`.

The first time it is `"Anna"`, then `"Bjørn"`, and finally `"Cecilie"`.

## Indentation shows what repeats

```python
for name in names:
    print("Hello")
    print(name)

print("Everyone has been processed")
```

Both indented lines run for each value.

The final line is not indented, so it runs only after the loop has finished.

## Follow the program step by step

For:

```python
values = [2, 4, 6]

for value in values:
    print(value)
```

this happens:

1. `value` becomes `2`, and the block runs
2. `value` becomes `4`, and the block runs
3. `value` becomes `6`, and the block runs
4. there are no more values, so the loop finishes

## A common error

This code is missing indentation:

```python
for value in values:
print(value)
```

Python expects an indented block after `for`.

Correct:

```python
for value in values:
    print(value)
```

Also notice the colon `:` after the `for` line.

## Change it

Change:

```python
names = ["Anna", "Bjørn", "Cecilie"]
```

to three different pieces of text.

First predict what the program will print. Then run it.

## Make it yourself

Create a program with three or more values and a `for` loop.

The program should:

- visit the values one at a time
- print each value
- have at least one additional instruction inside the loop
- print a final message after the loop

## What you learned

You can now:

- explain why loops are useful
- read a simple `for` loop
- explain that the loop variable receives one value at a time
- identify which instructions repeat by their indentation
- see when the loop has finished

The next lesson uses `range()` to repeat code a specific number of times.
