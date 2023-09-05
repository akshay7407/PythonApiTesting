#In Python, function is a group of related statements that perform a specific task.
#Function Declaration


def GreetMe(name):
    print("Good Morning"+name)
    data = input("Please enter user name : -")
    print(data)
    #Function Call


def AddIntegers(a, b):
    return a+b

GreetMe("Rahul Shetty")

print(AddIntegers(2, 3))

# Positional Arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 25)

# Keyword Arguments
greet(age=30, name="Bob")

# Default Arguments
def greet_default(name, age=18):
    print(f"Hello, {name}! You are {age} years old.")

greet_default("Charlie")  # Uses default age of 18

# Arbitrary Positional Arguments (*args)
def print_args(*args):
    for arg in args:
        print(arg)

print_args("apple", "banana", "cherry","moon")

# Arbitrary Keyword Arguments (**kwargs)
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_kwargs(name="Alice", age=25, city="New York")

# Combining Argument Types
def complex_function(a, b, *args, x=0, y=0, **kwargs):
    print("a:", a)
    print("b:", b)
    print("*args:", args)
    print("x:", x)
    print("y:", y)
    print("**kwargs:", kwargs)

complex_function(1, 2, 3, 4, x=10, y=20, key1="value1", key2="value2")







