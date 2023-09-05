

listItem= [2, 0, 88, 99, "akshay"]

#for in loop
for obj in listItem:
    print(obj)

#print 1 to 10 number in loop

for num in range(1, 11):
    print(num)

# sum of First Natural numbers 1+2+3+4+5 = 15
#range(i,j) -> i to j-1
summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)

print("*******************************")
for k in range(1, 10, 5):
    print(k)
    print("**************SKIPPING FIRST INDEX*****************")
for m in range(10):
    print(m)

# for loop  with increment value
print("**************increment value*****************")
for d in range(1,11,2):
    print(d)

# for loop  with decrement value
print("**************decrement  value*****************")
for d in range(11,0,-2):
    print(d)

# While loop with increment and decrement example

# Incrementing while loop
count = 0
while count < 5:
    print("Incrementing loop:", count)
    count += 1

# Decrementing while loop
count = 10
while count > 0:
    print("Decrementing loop:", count)
    count -= 2



