# Defining a dictionary
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
}


# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])

# Adding and updating entries
student["university"] = "ABC University"
student["age"] = 27

# Removing an entry
del student["major"]

# Dictionary methods
keys = student.keys()
values = student.values()
items = student.items()

print("Keys:", keys)
print("Values:", values)
print("Items:", items)
print("students", student)
