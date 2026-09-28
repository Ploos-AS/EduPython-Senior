# M3.1 – Let the user enter something

Until now, every value has been written into the program in advance. Now the program can ask the user.

Python's `input()` function pauses the program and waits for the user to type something.

## Try it

```python
name = input("What is your name? ")
print("Hello!")
print(name)
```

When the program reaches `input()`:

1. the text `What is your name? ` is displayed
2. the program waits
3. you type an answer and press Enter
4. the answer is stored in the variable `name`
5. the program continues

## input() returns text

This is important:

**`input()` always returns text.**

Try:

```python
age = input("How old are you? ")
print(age)
```

If you enter `70`, Python has received the text `"70"`, not the number `70`.

That is not an error. It is how `input()` works.

## Change it

Create a program that asks for two things:

```python
name = input("Name: ")
place = input("Place: ")

print("You entered:")
print(name)
print(place)
```

Change the questions to something else.

## Text can be used directly

When the answer really is text, no conversion is needed:

```python
interest = input("Enter something you enjoy learning about: ")
print("You entered:")
print(interest)
```

## What about calculations?

This may look natural:

```python
number = input("Enter a number: ")
print(number + 1)
```

but it does not work.

`number` contains text. Python cannot simply add the number `1` to a string.

In the next lesson, we learn to turn text such as `"42"` into the number `42`.

## Make it yourself

Create a small questionnaire that:

- asks at least three questions
- stores each answer in a variable
- prints the answers again with explanatory text

Use text answers only for now.

## What you learned

You can now:

- use `input()`
- store the user's answer in a variable
- explain that the program waits at `input()`
- explain that the result from `input()` is text

The next lesson turns text input into numbers we can calculate with.
