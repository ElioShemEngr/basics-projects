import sys

print("Marvel Movie Character Creator")
print("--")

response_1: str = input("Your super power is the spider web?: ")

if response_1 == "yes":
    print("You are Spider Man")
    sys.exit()
else:
    print("Then you're not Spider Man")
    print("Ok, next questions...")
print("")

response_2: str = input("You are a big man green?: ")

if response_2 == "yes":
    print("you are Hulk")
    sys.exit()
else:
    print("Then you're not Hulk")
    print("Ok, next questions...")
print("")

response_3: str = input("You are an engineer?: ")

if response_3 == "yes":
    print("you are Iron Man")
else:
    print("Then you're Iron Man")
    print("Ok, I give up on you...")
print("")
