"""
Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
"""
zoo = ["Monkey", "Tiger", "Giraffe", "Elephant", "Lion"]

zoo.append("Eagle")
print(zoo)
"""Delete the animal at the 3rd index."""
zoo.pop(3)
zoo.sort()
print(zoo)
"""Delete the animal at the beginning of the list."""
zoo.pop(0)
print(zoo)
# Print only the first 3 animals
print(zoo[0:3])

for x in zoo:
    print(x)