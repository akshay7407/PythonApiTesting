# Equality (==)
string1 = "apple"
string2 = "Apple"
string3 = "apple"

print(string1 == string2)  # False
print(string1 == string3)  # True

# Inequality (!=)
string1 = "apple"
string2 = "banana"

print(string1 != string2)  # True

# Greater Than (>) and Less Than (<)
string1 = "apple"
string2 = "banana"

print(string1 > string2)  # False
print(string1 < string2)  # True

# Greater Than or Equal To (>=) and Less Than or Equal To (<=)
string1 = "apple"
string2 = "banana"
string3 = "apple"

print(string1 >= string2)  # False
print(string1 <= string2)  # True
print(string1 <= string3)  # True

# Case-insensitive comparison
string1 = "Apple"
string2 = "apple"

print(string1.lower() == string2.lower())  # True (case-insensitive comparison)
