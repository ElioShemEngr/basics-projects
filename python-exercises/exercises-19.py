print("List Generator")
print()

startNumber = int(input("Input Start number > "))
endNumber = int(input("Input End number > "))
increment = int(input("Input increment > "))

counter = 1
for i in range(startNumber, endNumber, increment):
    print("Pos ",counter , " = ", i)
    counter += 1
