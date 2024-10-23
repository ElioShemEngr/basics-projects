print("Loan Calculator")
print()

loan = int(input("Loan Amount > "))
interest = int(input("Interest Percent > "))
time = int(input("Number of installments > "))

quotes = (loan + ((interest*loan)/100)) / time

for i in range(time+1):
    print("Day ", i+1, "= ", quotes, "Soles")
