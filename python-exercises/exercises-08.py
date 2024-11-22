print ("wholesome Positivity Machine")
print ()

nameUser: str = input ("Who are you?: ")
print ()

response: str = input ("What do you want to achieve today?: ")
print ()

scale: str = input ("On Scale of 1 - 10 how do you feel today? (1: 😢,10:🥳): ")
if scale == "1" or scale == "2" or scale == "3":
  print ("Hey ", nameUser, "keep your chin up! Today you're going to ", response, "in the most amazing way, simply by being you - YOU ROCK!")
elif scale == "4" or scale == "5" or scale == "6":
  print ("Hey ", nameUser, "You're going on!")
else:
  print ("Hey ", nameUser, "Perfect, thank you for that 🥳")
