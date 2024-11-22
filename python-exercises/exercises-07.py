print ("Fake Fan Finder")
print ("---------------")
print ()

anime: str = input("What is your favorite anime?: ")
if anime == "dragon ball":
  print("Oh, it's really cool!")
  faveCharacter: str = input("Name me any of the characters?: ")
  if faveCharacter == "goku":
    powerName1: str = input ("you got by pure chance. Okay then, what is the name her power?:")
    if powerName1 == "kamehame ha":
      print("You are true fan!")
    elif powerName1 == "henki dama":
      print("You are true fan!, but hamehame ha is the best")
    else:
      print("Nah, You are Fake Fan")
  elif faveCharacter == "vegeta":
    print("Aww, he is the best character")
  else:
    print("Nah, goku's the greatest")
elif anime == "naruto":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")
