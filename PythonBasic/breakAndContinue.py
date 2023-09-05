# Break statement example
for num in range(1, 11):
    if num == 5:
        print("Breaking the loop at", num)
        break
    print("Current number:", num)

# Continue statement example
for num in range(1, 6):
    if num == 3:
        print("Skipping iteration for", num)
        continue
    print("Current number:", num)
