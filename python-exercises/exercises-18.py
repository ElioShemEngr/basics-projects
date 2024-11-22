print("Loan Calculator")
print()

loan: int = int(input("Loan Amount > "))
interest: int = int(input("Interest Percent > "))
time: int = int(input("Number of installments > "))

quotes: float = (loan + ((interest*loan)/100)) / time

for i in range(time+1):
    print("Day ", i+1, "= ", quotes, "Soles")
