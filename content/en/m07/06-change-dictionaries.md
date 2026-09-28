# M7.6 – Change a dictionary

Dictionaries can be changed after they are created.

We use the same basic form both when we:

- change a value that already exists
- add a new key and value

## Try it – change an existing value

\`\`\`python
person = {
    "name": "Anna",
    "age": 72
}

person["age"] = 73

print(person)
\`\`\`

The result now contains:

\`\`\`text
'age': 73
\`\`\`

The key \`"age"\` already existed, so its value was replaced.

## Read the assignment

This line:

\`\`\`python
person["age"] = 73
\`\`\`

can be read as:

> set the value for the key "age" in person to 73

This resembles how we changed a list:

\`\`\`python
temperatures[1] = 21
\`\`\`

The difference is what appears inside the square brackets:

- list: index
- dictionary: key

## Add a new key

If the key does not exist, it is created:

\`\`\`python
person = {
    "name": "Anna",
    "age": 72
}

person["place"] = "Grimstad"

print(person)
\`\`\`

The dictionary now also contains:

\`\`\`text
'place': 'Grimstad'
\`\`\`

We used exactly the same syntax:

\`\`\`python
dictionary[key] = value
\`\`\`

## Existing or new key?

Look at:

\`\`\`python
person["age"] = 73
person["place"] = "Grimstad"
\`\`\`

If the key exists:

**the value is updated**

If the key does not exist:

**a new key/value pair is added**

## Build an empty dictionary

We can start with:

\`\`\`python
book = {}
\`\`\`

and add information over time:

\`\`\`python
book["title"] = "Python for Everyone"
book["pages"] = 200
book["language"] = "English"

print(book)
\`\`\`

This is useful when information becomes available at different times in a program.

## Use a variable as the value

The value does not have to appear directly in the assignment:

\`\`\`python
person = {
    "name": "Anna"
}

new_age = 73
person["age"] = new_age

print(person["age"])
\`\`\`

Result:

\`\`\`text
73
\`\`\`

## Use a function

A function can read from a dictionary:

\`\`\`python
def show_person(person):
    print("Name:", person["name"])
    print("Place:", person["place"])


person = {
    "name": "Anna",
    "place": "Grimstad"
}

show_person(person)
\`\`\`

The complete dictionary is passed as an argument.

The parameter \`person\` refers to the dictionary while the function runs.

## A function can return a value from the dictionary

\`\`\`python
def get_name(person):
    return person["name"]


person = {
    "name": "Anna",
    "age": 72
}

name = get_name(person)
print(name)
\`\`\`

Result:

\`\`\`text
Anna
\`\`\`

This connects dictionaries with what you learned about functions in M6.

## Be precise with key names

These are different:

\`\`\`python
person["name"]
person["Name"]
\`\`\`

If only \`"name"\` exists, \`"Name"\` will produce a \`KeyError\`.

When updating a dictionary, it is therefore important to spell the key exactly as intended.

## Change it

Start with:

\`\`\`python
book = {
    "title": "Python for Everyone",
    "pages": 200
}
\`\`\`

Do the following:

1. change \`"pages"\` to another value
2. add the key \`"language"\`
3. print each of the three values
4. print the complete dictionary

## Make it yourself

Start with an empty dictionary.

Add at least three key/value pairs.

Then change the value of one key that already exists.

Create a small function that accepts the dictionary and prints or returns at least one of its values.

## What you learned

You can now:

- change the value of an existing key
- add a new key and value
- explain that both use \`dictionary[key] = value\`
- build an empty dictionary
- use variables as new values
- pass a dictionary to a function
- read and return dictionary values from a function
- pay attention to exact key names

The next lesson combines lists and dictionaries in a practical example.
