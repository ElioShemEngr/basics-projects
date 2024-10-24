import random

print("IDEAS")
print("-----")
print("1: Add an idea")
print("2: Load up a random idea")
print()
select = input("> ")

if select == "1":
    f = open("ideas.txt", "a+")
    userIdea = input("Idea > ")
    idea = f.write(f"{userIdea} \n")
    f.close()
elif select == "2":
    f = open("ideas.txt", "r")
    ideas = f.read().split("\n")
    ideasOK = []
    for row in ideas:
        if row != '':
            ideasOK.append(row)
    number = len(ideasOK)
    randomIdea = random.randint(0,number-1)
    print(ideasOK[randomIdea])

    f.close()