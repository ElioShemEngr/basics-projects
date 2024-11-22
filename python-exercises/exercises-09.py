print("Generation Identifier")
print("---------------------")
print()

nameUser: str = input("What's your name?: ")
yearBirth: int = int(input("Which year were you born?: "))
if yearBirth >=1883 and yearBirth <=1900:
  print("Hah!", nameUser, ", You are the Lost Generation")
elif yearBirth >=1901 and yearBirth <=1927:
  print("Hah!", nameUser, ", You are the Greatest Generation")
elif yearBirth >=1928 and yearBirth <=1945:
  print("Hah!", nameUser, ", You are Silent Generation")
elif yearBirth >=1946 and yearBirth <=1964:
  print("Hah!", nameUser, ", You are Baby Boomers")
elif yearBirth >=1965 and yearBirth <=1980:
  print("Hah!", nameUser, ", You are the Generation X")
elif yearBirth >=1981 and yearBirth <=1996:
  print("Hah!", nameUser, ", You are the Millenials")
elif yearBirth >=1997 and yearBirth <=2012:
  print("Hah!", nameUser, ", You are Generation Z")
elif yearBirth >=2013 and yearBirth <=2023:
  print("Hah!", nameUser, ", You are Generation Alpha")
else:
  print("In outer year please")
