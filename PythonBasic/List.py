# Creating a list
fruits = ["apple", "banana", "orange", "grape"]

# Inserting data
fruits.append("pear")
fruits.insert(1, "kiwi")
fruits[2] = "pineapple"

# Fetching data
print("all fruit:", fruits)
print("First fruit:", fruits[0])  # "apple"
print("Third fruit:", fruits[2])  # "pineapple"

# Updating data
fruits[3] = "mango"

# Removing data
fruits.remove("kiwi")
removed_fruit = fruits.pop(2)
del fruits[0]

print("Updated list:", fruits)
print("Removed fruit:", removed_fruit)

# Creating a list of strings
fruits = ["apple", "banana", "orange", "grape"]

# Concatenating strings in the list
concatenated = "-".join(fruits)
print("Concatenated:", concatenated)

# Finding the length of each string in the list
lengths = [len(fruit) for fruit in fruits]
print("Lengths of strings:", lengths)


data = [1, 2, 3, "akshay", 8.0]

print(data)
print(data[2])
#append the list data
data.append("Gaikwad")
print(data)
#insert the value in list at position 3

data.insert(3, "Pune")
print(data)

#print list 1 to 3 where 1 is inclusive and 3 is exclusive
print(data[1:3])


#Tuple are imutuable cant redefined the values

tup = ("char", "float", 88, 00)
print(tup)
