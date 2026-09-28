# M7.5 – Find values by name: dictionaries

A list works well when we have several values in an order.

But sometimes the values describe different things.

Look at this list:

\`\`\`python
person = ["Anna", 72, "Grimstad"]
\`\`\`

What do indexes 0, 1, and 2 mean?

We can learn that:

- 0 is the name
- 1 is the age
- 2 is the place

But Python has a collection type where we can use **names** instead.

It is called a **dictionary**.

## Try it

\`\`\`python
person = {
    "name": "Anna",
    "age": 72,
    "place": "Grimstad"
}

print(person)
\`\`\`

The dictionary contains three pieces of information about the person.

## Key and value

Look at:

\`\`\`python
"name": "Anna"
\`\`\`

Here:

\`\`\`text
"name"  → key
"Anna"  → value
\`\`\`

Such a pair is called a **key/value pair**.

The dictionary:

\`\`\`python
person = {
    "name": "Anna",
    "age": 72,
    "place": "Grimstad"
}
\`\`\`

can be read as:

\`\`\`text
name  → Anna
age   → 72
place → Grimstad
\`\`\`

## Retrieve a value with its key

To retrieve the name:

\`\`\`python
print(person["name"])
\`\`\`

Result:

\`\`\`text
Anna
\`\`\`

To retrieve the age:

\`\`\`python
print(person["age"])
\`\`\`

Result:

\`\`\`text
72
\`\`\`

We still use square brackets, but now they contain a **key**, not a numbered index.

## Lists and dictionaries solve different problems

List:

\`\`\`python
temperatures = [18, 20, 17]
\`\`\`

Here, order matters and we can use indexes:

\`\`\`python
temperatures[0]
\`\`\`

Dictionary:

\`\`\`python
person = {
    "name": "Anna",
    "age": 72
}
\`\`\`

Here, we find values using descriptive keys:

\`\`\`python
person["name"]
\`\`\`

It is not a question of one type always being better. They describe different kinds of data.

## Curly braces

Lists use:

\`\`\`text
[ ]
\`\`\`

Dictionaries use:

\`\`\`text
{ }
\`\`\`

Example:

\`\`\`python
book = {
    "title": "Python",
    "pages": 250
}
\`\`\`

The colon \`:\` separates the key from the value.

Commas separate the key/value pairs.

## What happens if the key does not exist?

\`\`\`python
person = {
    "name": "Anna",
    "age": 72
}

print(person["phone"])
\`\`\`

Python reports an error containing:

\`\`\`text
KeyError: 'phone'
\`\`\`

This means the program tried to retrieve a key that does not exist in the dictionary.

## Read KeyError

When you see \`KeyError\`, ask:

1. Which dictionary am I using?
2. Which key am I trying to retrieve?
3. Does the key exist in the dictionary?
4. Is the key spelled exactly the same way?

For example:

\`\`\`text
"name"
\`\`\`

and:

\`\`\`text
"Name"
\`\`\`

are two different text values.

## An empty dictionary

We can also create an empty dictionary:

\`\`\`python
information = {}

print(information)
\`\`\`

Result:

\`\`\`text
{}
\`\`\`

In the next lesson, we will learn how to add and change key/value pairs.

## Change it

Start with:

\`\`\`python
book = {
    "title": "Python for Everyone",
    "pages": 200,
    "language": "English"
}
\`\`\`

Print:

- the complete dictionary
- the title
- the number of pages
- the language

Then deliberately try a key that does not exist. Read the \`KeyError\`, correct the key, and run the program again.

## Make it yourself

Create a dictionary describing one thing, such as a book, an appointment, a city, or a measurement.

Use at least three key/value pairs.

Print the complete dictionary and then each value using its key.

## What you learned

You can now:

- explain the difference between a list index and a dictionary key
- create a dictionary with \`{\` and \`}\`
- recognise a key/value pair
- retrieve a value using a key
- explain why descriptive keys can make data easier to understand
- recognise and investigate \`KeyError\`
- create an empty dictionary

The next lesson is about changing existing values and adding new keys.
