str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[1])   #a

print(str[0:5])  # if you want substring in python

print(str+str1)   # concatenation

# Fetching a substring using slicing
original_string = "Hello, World!"

# Extracting a substring from index 7 to index 11
substring = original_string[7:12]

print("Original String:", original_string)
print("Substring:", substring)

text = "Hello, World!"
length = len(text)
print("Length of the string:", length)

text = "hello, world!"
capitalized_text = text.capitalize()
print("Original text:", text)
print("Capitalized text:", capitalized_text)

text = "hello, world!"
uppercase_text = text.upper()
print("Original text:", text)
print("Uppercase text:", uppercase_text)

text = "Hello, World!"
lowercase_text = text.lower()
print("Original text:", text)
print("Lowercase text:", lowercase_text)

# The lstrip() method is used to remove leading (left) whitespace or specified characters from the beginning of a string.
text = "$$$Hello, World!"
stripped_text = text.lstrip("$")
print("Original text:", text)
print("Stripped text:", stripped_text)

# The rstrip() method is used to remove trailing (right) whitespace or specified characters from the end of a string.

text = "   Hello, World!   "
stripped_text = text.rstrip()
print("Original text:", text)
print("Stripped text:", stripped_text)

text = "Hello, World!$$$"
stripped_text = text.rstrip("$")
print("Original text:", text)
print("Stripped text:", stripped_text)

# The strip() method is used to remove both leading and trailing whitespace or specified characters from a string.

text = "   Hello, World!   "
stripped_text = text.strip()
print("Original text:", text)
print("Stripped text:", stripped_text)

text = "$$$Hello, World!$$$"
stripped_text = text.strip("$")
print("Original text:", text)
print("Stripped text:", stripped_text)











