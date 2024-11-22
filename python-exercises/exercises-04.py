print("\033[31m","=== Your Adventure Simulator ===","\033[0m")

print("""Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!""")
print()

name: str = input("What is your name?: ")
enemy: str = input("What is your worst enemy’s name?: ")
superPower: str = input("What is your superpower?: ")
print()

print("\033[33m", "Our Story begins as our hero name approaches a foreboding castle...", "\033[0m",)
print("Suddenly a bolt of ligthning striked the ground at the feet of", "\033[34m", name, "\033[0m")
print("'Our final battle begins!' shouts the evil","\033[32m", enemy, "\033[0m", "clearly missing the fact that", "\033[34m", name, "\033[0m", "has the power of", "\033[35m", superPower, "\033[0m","Which means they'll win quite easily...")
print("\033[2mThis story continue...\033[0m")
