# M7.8 – Exercises and mini-project

Now you will use lists and dictionaries without every step being shown in advance.

A useful working order is:

1. predict what the program will do
2. run the program
3. compare the result with your prediction
4. investigate any errors
5. change the program

## Exercise 1 – Read a list

What does this program print?

\`\`\`python
prices = [12, 18, 25, 9]

print(prices[0])
print(prices[2])
print(len(prices))
\`\`\`

Predict the result before running it.

## Exercise 2 – Find the error

\`\`\`python
places = ["Tonstad", "Grimstad", "Oslo"]

print(places[3])
\`\`\`

Run the program and read the error message.

Answer:

- what type of error do you get?
- how many items are there?
- which indexes are valid?
- which index retrieves Oslo?

Correct the program.

## Exercise 3 – Change the list

Start with:

\`\`\`python
temperatures = [17, 19, 18]
\`\`\`

Do the following:

1. change the second value to 20
2. add 21 with \`append()\`
3. print the number of items with \`len()\`
4. use a \`for\` loop to print all temperatures

## Exercise 4 – Read a dictionary

What does the program print?

\`\`\`python
book = {
    "title": "Python in Practice",
    "pages": 240,
    "language": "English"
}

print(book["title"])
print(book["pages"])
\`\`\`

Then change the page count and add the key \`"year"\`.

## Exercise 5 – Find KeyError

The program contains an error:

\`\`\`python
appointment = {
    "day": "Friday",
    "time": "14:00"
}

print(appointment["clock"])
\`\`\`

Run the program.

Read the \`KeyError\` and compare the key in the error message with the keys that actually exist.

Correct the program without changing the dictionary.

## Exercise 6 – List or dictionary?

Choose the data structure that fits best.

A. Temperature measurements in sequence.

B. Information about one book: title, author, and page count.

C. Names of five places that you want to process one at a time.

D. Information about one appointment: date, time, and place.

Explain your choices in your own words.

## Exercise 7 – Follow the structure

\`\`\`python
measurements = [
    {"day": "Monday", "kwh": 10},
    {"day": "Tuesday", "kwh": 12}
]

first = measurements[0]
print(first["day"])
print(first["kwh"])
\`\`\`

Explain what happens in two steps:

1. What does \`first\` contain?
2. What does \`first["day"]\` do?

## Exercise 8 – Calculate the total

Complete the function:

\`\`\`python
def calculate_total(measurements):
    total = 0

    for measurement in measurements:
        # add the kWh value to total here

    return total
\`\`\`

Test it with:

\`\`\`python
measurements = [
    {"day": "Monday", "kwh": 10},
    {"day": "Tuesday", "kwh": 12},
    {"day": "Wednesday", "kwh": 9}
]

print(calculate_total(measurements))
\`\`\`

Expected result:

\`\`\`text
31
\`\`\`

## Mini-project – A small expense register

Create a program that keeps track of a few expenses.

Start with:

\`\`\`python
expenses = [
    {"description": "Bus", "amount": 45},
    {"description": "Coffee", "amount": 38},
    {"description": "Book", "amount": 249}
]
\`\`\`

The program should:

1. print each description and amount
2. calculate the total amount in a function
3. return the total from the function
4. print the total
5. add one new expense with \`append()\`
6. calculate and print the new total

Here is the shape of the function:

\`\`\`python
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    return total
\`\`\`

Try to write the rest yourself first.

## Extend the mini-project

When the basic version works, try one or more changes:

- change the amount of an existing expense
- print how many expenses there are
- add a new key, such as \`"category"\`
- use \`if\` inside the loop to print only expenses above a chosen amount

Make one change at a time and run the program after each change.

## Debugging round

If the program stops, first look at the name of the error.

\`IndexError\`:

- inspect the list index
- remember that the first index is 0
- compare the index with \`len(list_name)\`

\`KeyError\`:

- inspect the key
- compare its spelling with the keys in the dictionary

If the program runs but the result is wrong:

- follow one loop iteration at a time
- optionally print \`total\` while the loop runs
- check which value is retrieved from each dictionary

## M7 is complete when you can

- create and read lists
- use indexes
- understand the relationship between \`len()\` and indexes
- change and extend lists
- create and read dictionaries
- use key/value pairs
- change and extend dictionaries
- recognise \`IndexError\` and \`KeyError\`
- combine lists and dictionaries
- use collections with loops and functions
- build a small program with structured data

The next milestone is about files and folders.
