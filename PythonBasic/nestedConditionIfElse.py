# Nested conditions example

# Assume we have a student's exam scores
math_score = 10
science_score = 92

# Outer condition
if math_score >= 90:
    # Nested condition 1
    if science_score >= 90:
        print("Congratulations! You've excelled in both Math and Science.")
    else:
        print("Great job in Math, but you could work on improving your Science score.")
elif math_score >= 80:
    # Nested condition 2
    if science_score >= 80:
        print("Good work! You've done well in both Math and Science.")
    else:
        print("You've done decently in Math, but Science needs more attention.")
else:
    # Nested condition 3
    if science_score >= 70:
        print("You should focus on improving your Math score, but Science is looking good.")
    else:
        print("Both Math and Science scores need improvement.")

# The above code will evaluate the student's scores in both Math and Science
# and provide feedback based on nested conditions.
