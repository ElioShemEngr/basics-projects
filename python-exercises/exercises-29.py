print("30 Days Down - What did you think?")

for i in range(1,31):
    print(f"Day {i}:")
    userWord = input("> ")
    print()
    response = f"You thougth Day {i} was"
    print(f"{response: ^50}")
    print(f"{userWord: ^50}")
    print()