print("List Generator")
print()

startNumber: int = int(input("Input Start number > "))
endNumber: int = int(input("Input End number > "))
increment: int = int(input("Input increment > "))

counter: int = 1
for i in range(startNumber, endNumber, increment):
    print("Pos ",counter , " = ", i)
    counter += 1
