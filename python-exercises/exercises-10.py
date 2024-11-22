print("--------------")
print("Tip Calculator")
print("--------------")
print()

spend: int = int(input("How much did you spend? > "))
tipPercent: int = int(input("what Percentage do you want to tip? > "))
numberPeople: int = int(input("How many people in your group? > "))

total: float = ( spend + (tipPercent * spend / 100 ) ) / numberPeople

print("You each owe ", total)
