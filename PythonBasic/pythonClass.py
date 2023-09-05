class Calculator:

    def __int__(self):
        print("I am the constructor")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"


# Creating an instance of the Calculator class
Calculator()
calculator = Calculator()

# Calling the functions
result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(10, 4)
result_multiply = calculator.multiply(6, 2)
result_divide = calculator.divide(10, 2)

# Displaying the results
print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
