print("--------------")
print("Tip Calculator")
print("--------------")
print()

spend = int(input("How much did you spend? > "))
tipPercent = int(input("what Percentage do you want to tip? > "))
numberPeople = int(input("How many people in your group? > "))

total = ( spend + (tipPercent * spend / 100 ) ) / numberPeople

print("You each owe ", total)
