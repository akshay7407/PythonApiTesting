# Condition handling with Logical OR and Logical AND example

# Assume we have a user's age and subscription status
user_age = 10
is_subscribed = True

# Logical OR example
if user_age < 18 or is_subscribed:
    print("You have access to the content.")
else:
    print("You need to be subscribed or over 18 to access the content.")

# Logical AND example
if user_age >= 18 and is_subscribed:
    print("Welcome! You are eligible to access all content.")
else:
    print("You need to be both subscribed and over 18 to access all content.")
