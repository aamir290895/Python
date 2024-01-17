person = {"name": "Aamir", "spouse": "Naushi", "age": 25}

print(person)

person.pop("name")  # pop will remove the key and its values from dictionary
person["name"] = "Aamir"

print(person)

del person['age']  # Removes the key and value "age";

print(person)

if "name" in person:
    print(person["name"])

for key, value in person.items():
    print(key, value)

k = person.get("spouse")

print(k)

for value in person.values():
    print(value)

