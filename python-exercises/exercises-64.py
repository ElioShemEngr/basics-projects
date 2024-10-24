print("CHARACTER CREATOR")
print()

class character:
    name = None
    hp = 100
    mp = 100
    
    def __init__(self, name: str):
        self.name = name
    
    def printPretty(self):
        print("Set Stats")
        print(f"{self.name}\nHP: {self.hp}\nMP: {self.mp}")
    
    def setStats(self, hp, mp):
        self.hp = hp
        self.mp = mp
        
class player(character):
    nickname = None
    lives = 3

    def __init__(self, nickname: str):
        self.name = "Player"
        self.nickname = nickname

    def printPretty(self):
        print("Set Stats")
        print(f"{self.name}\nHP: {self.hp}\nMP: {self.mp}\nNickname: {self.nickname}\nLives: {self.lives}")

    def isAlive(self):
        if self.lives <= 0:
            print("You are dead!!!")
            return False
        else:
            print(f"You have {self.lives} lives")
            return True

class enemy(character):
    type = None
    strength = None

    def __init__(self, name: str, type: str, strength: int):
        self.name = name
        self.type = type
        self.strength = strength

    def printPretty(self):
        print("Set Stats")
        print(f"{self.name}\nHP: {self.hp}\nMP: {self.mp}\nNickname: {self.type}\nLives: {self.strength}")

class orc(enemy):
    speed = None

    def __init__(self, speed: int):
        self.name = "Orc"
        self.type = "Orc"
        self.strength = 200
        self.speed = speed

    def printPretty(self):
        print("Set Stats")
        print(f"{self.name}\nHP: {self.hp}\nMP: {self.mp}\nNickname: {self.type}\nLives: {self.strength}\n Speed: {self.speed}")

class vampire(enemy):
    day = True

    def __init__(self, day: bool):
        self.name = "Vampire"
        self.type = "Vampire"
        self.strength = 200
        self.day = day

    def printPretty(self):
        print("Set Stats")
        print(f"{self.name}\nHP: {self.hp}\nMP: {self.mp}\nNickname: {self.type}\nLives: {self.strength}\n Day: {self.day}")


ian = player("Ian the mighty")
ian.printPretty()
print(ian.isAlive())

