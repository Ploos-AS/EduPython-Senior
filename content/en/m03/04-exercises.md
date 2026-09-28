# M3.4 – Exercises and debugging

These exercises bring M3 together. Try each one before reading the guidance.

## 1. What is stored?

Look at:

```python
answer = input("Enter 25: ")
```

If the user enters `25`, is `answer` text or a number?

**Guidance:** Think about what `input()` always returns.

**Answer:** `answer` contains the text `"25"`.

## 2. Turn the text into an integer

Complete:

```python
quantity_text = input("Quantity: ")
quantity = __________

print(quantity + 1)
```

**Possible solution:**

```python
quantity = int(quantity_text)
```

## 3. Choose int or float

Which conversion is most appropriate?

- number of books
- temperature
- number of days
- price per kWh
- distance in kilometres

**Guidance:** Values that may need decimals often suit `float()`. Whole counts often suit `int()`.

One reasonable choice is:

- number of books → `int()`
- temperature → `float()`
- number of days → `int()`
- price per kWh → `float()`
- distance → `float()`

## 4. Find the problem

The program should add one to the user's number:

```python
number = input("Number: ")
result = number + 1
print(result)
```

Why does it not work?

**Answer:** `number` is text. Convert it first:

```python
number = int(input("Number: "))
result = number + 1
print(result)
```

## 5. Read ValueError

The program is:

```python
price = float(input("Price: "))
print(price)
```

The user enters:

```text
cheap
```

Python stops with `ValueError`.

Explain in your own words why.

**Answer:** `float()` received text that does not represent a valid number. Python received a value, but could not convert it as the program requested.

## 6. Calculate with two user values

Create a program that asks for:

- quantity
- price per item

Calculate the total price and print it.

**Possible solution:**

```python
quantity = int(input("Quantity: "))
price = float(input("Price per item: "))

total = quantity * price

print("Total:")
print(total)
```

## 7. Mini-project

Build your own interactive calculator.

Requirements:

- at least two `input()` calls
- clear variable names
- appropriate use of `int()` or `float()`
- at least one calculation
- store the result in a variable
- print explanatory text
- the program should run with different valid values without changing its source code

Possible themes include distance, time, price, energy use, temperature, or another subject you choose.

## Before moving on

You should now be able to explain:

- why `input()` returns text
- how text becomes an integer
- how text becomes a floating-point number
- why invalid numeric text can produce `ValueError`
- how user data can be used in a calculation

The next milestone introduces decisions: programs will be able to do different things depending on a condition.
