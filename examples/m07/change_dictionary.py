person = {
    "name": "Anna",
    "age": 72,
}

person["age"] = 73
person["place"] = "Grimstad"

print(person)


def get_name(person):
    return person["name"]


print(get_name(person))
