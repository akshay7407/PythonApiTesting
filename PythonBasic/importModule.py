import  pymodule

class ImportModule:
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

    # Creating an instance of the Calculator class


calculator = ImportModule()
thisClass = calculator.divide(14,7)
print(thisClass)
moduleCal = pymodule.add(9,9)
print("Imported module  : "+ str(moduleCal))