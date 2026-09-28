# M6.7 – Exercises and debugging

These exercises bring all of M6 together. Try to predict the result before running the code.

## 1. Definition or call?

What does this code do?

\`\`\`python
def say_hello():
    print("Hello!")
\`\`\`

**Answer:** It defines the function. It does not call it.

To run the function:

\`\`\`python
say_hello()
\`\`\`

## 2. How many times?

\`\`\`python
def show_message():
    print("Python")

show_message()
show_message()
show_message()
\`\`\`

How many times is \`Python\` printed?

**Answer:** Three times.

## 3. Find the indentation error

\`\`\`python
def show_name():
print("Anna")
\`\`\`

**Answer:** The function block must be indented:

\`\`\`python
def show_name():
    print("Anna")
\`\`\`

## 4. Follow the parameter

\`\`\`python
def show_double(number):
    print(number * 2)

show_double(7)
\`\`\`

What is the value of \`number\` inside the function?

**Answer:** \`7\`.

What is printed?

**Answer:** \`14\`.

## 5. Multiple parameters

\`\`\`python
def calculate(price, quantity):
    return price * quantity

result = calculate(20, 3)
print(result)
\`\`\`

What is the result?

**Answer:** \`60\`.

## 6. print or return?

Look at:

\`\`\`python
def calculate(price, quantity):
    print(price * quantity)
\`\`\`

The function displays the result, but does not give it back with \`return\`.

If the rest of the program should use the result, we can write:

\`\`\`python
def calculate(price, quantity):
    return price * quantity
\`\`\`

Explain in your own words the difference between **displaying** a value and **returning** a value.

## 7. What happens after return?

\`\`\`python
def test():
    print("A")
    return 5
    print("B")

result = test()
print(result)
\`\`\`

What is printed?

**Answer:**

\`\`\`text
A
5
\`\`\`

\`print("B")\` does not run because \`return\` ends the function.

## 8. Find the logic error

The function should calculate price times quantity:

\`\`\`python
def calculate_total(price, quantity):
    return price + quantity
\`\`\`

The code is valid Python, but the calculation is wrong.

**Correction:**

\`\`\`python
def calculate_total(price, quantity):
    return price * quantity
\`\`\`

## 9. A decision in a function

\`\`\`python
def category(number):
    if number < 0:
        return "negative"
    else:
        return "zero or positive"

print(category(-2))
print(category(0))
\`\`\`

What is printed?

**Answer:**

\`\`\`text
negative
zero or positive
\`\`\`

## 10. Function and loop

\`\`\`python
def square(number):
    return number * number

for number in range(1, 4):
    print(square(number))
\`\`\`

What is printed?

**Answer:**

\`\`\`text
1
4
9
\`\`\`

## 11. Test boundary values

You have the function:

\`\`\`python
def calculate_total(price, quantity):
    return price * quantity
\`\`\`

Create at least three tests.

Include:

- a normal value
- \`quantity = 1\`
- \`quantity = 0\`

Write the expected result before running the code.

## 12. Mini-project

Create a small program with at least two functions.

Requirements:

- at least one function has a parameter
- at least one function returns a value
- use a decision or loop in or together with a function
- use a returned result elsewhere in the program
- test at least one function separately with several values
- give the functions names that describe their jobs

Possible themes include costs, electricity use, distances, time use, or other simple calculations.

## Before moving on

You should now be able to explain:

- why functions are useful
- the difference between defining and calling a function
- what a parameter does
- how values are passed into a function
- the difference between \`print()\` and \`return\`
- how a returned result is used elsewhere
- that \`return\` ends a function
- how \`if\` and loops can work with functions
- why small functions can be easier to test
- how known test values can reveal a logic error

The next milestone is about lists and dictionaries: working with collections of data.
