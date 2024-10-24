
myString = input("What sentence do you want rainbow-ising? > ")
for letter in myString:
    if letter.lower() == "r":
        print('\033[31m', end ='') #Red
    if letter.lower() == "b":
        print('\033[34m', end ='') #Blue
    if letter.lower() == "y":
        print('\033[33m', end ='') #Yellow
    if letter == " ":
        print('\033[0m', end ='') #Back to default
    print(letter, end = '')
    
