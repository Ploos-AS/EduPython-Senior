# M6.6 – Test one function at a time

When a program does not work as expected, it can be difficult to find the error if everything is in one large block of code.

Small functions make it easier to examine one part at a time.

## Try it

Look at this function:

\`\`\`python
def calculate_total(price, quantity):
    return price * quantity
\`\`\`

We can test it with known values:

\`\`\`python
print(calculate_total(10, 3))
print(calculate_total(25, 4))
\`\`\`

We expect:

\`\`\`text
30
100
\`\`\`

If the result is different, we know to investigate the calculation itself.

## Test with simple values

When debugging, it is often useful to begin with values where the answer is easy to calculate yourself.

For example:

\`\`\`python
calculate_total(10, 3)
\`\`\`

is easy to check:

\`\`\`text
10 × 3 = 30
\`\`\`

Then we can try more realistic values.

## A function can have a small test section

\`\`\`python
def calculate_total(price, quantity):
    return price * quantity


print("Test 1:", calculate_total(10, 3))
print("Test 2:", calculate_total(25, 4))
\`\`\`

This is not an advanced testing tool. It is simply an easy way to examine the function.

## Find a logic error

Look at:

\`\`\`python
def calculate_total(price, quantity):
    return price + quantity
\`\`\`

If we test:

\`\`\`python
print(calculate_total(10, 3))
\`\`\`

we get 13.

But if the function should calculate price times quantity, we expect 30.

The program can therefore be valid Python and still have incorrect logic.

Correct:

\`\`\`python
def calculate_total(price, quantity):
    return price * quantity
\`\`\`

## Test the function before the rest of the program

Suppose the main program is:

\`\`\`python
price = 25
quantity = 4

total = calculate_total(price, quantity)
print("Total:", total)
\`\`\`

If the total is wrong, first test:

\`\`\`python
print(calculate_total(25, 4))
\`\`\`

This examines the function without the rest of the program.

## Test different situations

For a simple calculation function, we can test:

**Normal value**

\`\`\`python
calculate_total(25, 4)
\`\`\`

**One item**

\`\`\`python
calculate_total(25, 1)
\`\`\`

**Zero**

\`\`\`python
calculate_total(25, 0)
\`\`\`

The last one can be useful because boundary values often reveal errors.

## Do not rely on only one test

If one test works, that does not necessarily mean the function always works.

Several small tests give better information.

## Change it

Create a function that performs a simple calculation.

Find at least three test values whose results you can calculate in advance.

Compare the Python result with what you expected.

## Make it yourself

Create a function that:

- has at least one parameter
- returns a result
- is tested with at least three different calls
- has at least one boundary-value test, such as 0 or 1

You can write the expected result as a comment before running the test.

## What you learned

You can now:

- test a function separately
- use simple values to check a calculation
- distinguish syntax errors from logic errors
- use several test values
- use boundary values in simple testing
- find an error in a small function before investigating the rest of the program

The next lesson brings M6 together with exercises and debugging.
