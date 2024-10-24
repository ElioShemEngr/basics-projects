print("Contact Card")
print()

name = input("Name > ")
dateBirth = input("Date Of Birth > ")
numberTel = input("Telephone Number > ")
email = input("Email > ")
address = input("Address > ")

dictName = {"name" : name, "dateBirth" : dateBirth , "numberTel" : numberTel, "email" : email, "address" : address}

print()
print("--------------------------")
print()
print("Here's your contact card")
print()
print(f" Name, {dictName['name']}")
print(f" DOB, {dictName['dateBirth']}")
print(f" Tel, {dictName['numberTel']}")
print(f" Email, {dictName['email']}")
print(f" Address, {dictName['address']}")

