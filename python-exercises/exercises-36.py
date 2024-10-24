print("STAR WARS NAME GENERATOR")
print()

userData = input("Enter your name, last name, Mum's maiden name and the city you were born in:").split()

firstName = userData[0]
lastName = userData[1]
mumsName = userData[2]
cityName = userData[3]

print(f"Your Star Wars name is {firstName[:3]}{lastName[0:2]} {mumsName[0:2]}{cityName[-3:]}")