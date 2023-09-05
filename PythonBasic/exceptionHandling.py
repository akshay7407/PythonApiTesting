try:
    # Try to perform the following operations
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Invalid input, please enter valid integers")
except Exception as e:
    print("An error occurred:", e)
else:
    print("No exceptions occurred.")
finally:
    print("Exception handling is complete.")

print("Program continues...")
