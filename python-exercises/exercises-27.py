import os, time

#Funtion for health
def heatlh():
  import random
  sideRoll6 = random.randint(0,6)
  sideRoll12 = random.randint(0,12)
  resultado = ((sideRoll6 * sideRoll12)/2)+10
  return resultado

#funtion for strength
def strength():
  import random
  sideRoll6 = random.randint(0,6)
  sideRoll12 = random.randint(0,12)
  resultado = ((sideRoll6 * sideRoll12)/2)+12
  return resultado

#funtion for 6-sided dice
def dice6sided():
  import random
  sideRoll6 = random.randint(0,6)
  return sideRoll6

print("⚔️⚔️ -BATTLE TIME-  ⚔️⚔️")#1RO CREAR LUCHADORES
print()

print("Name Your Legend : ")
nameLegend_1 = input("-> ")
print()
print("Character Type (Human, Elf, Wizard, Orc):")
characterType_1 = input("-> ")
health_user1 = heatlh()
strength_user1 = strength()

print("----------PLAYER 1----------")
print("NickName   : ", nameLegend_1)
print("Type       : ", characterType_1)
print("Health     : ", health_user1)
print("Strength   : ", strength_user1)
print("----------------------------") 
print()

print("Who are they battling?")
  
print()
print("Name Your Legend : ")
nameLegend_2 = input("-> ")
print()
print("Character Type (Human, Elf, Wizard, Orc):")
characterType_2 = input("-> ")
health_user2 = heatlh()
strength_user2 = strength()

print("----------PLAYER 2----------")
print("NickName   : ", nameLegend_2)
print("Type       : ", characterType_2)
print("Health     : ", health_user2)
print("Strength   : ", strength_user2)
print("----------------------------") 
print()
time.sleep(5)
os.system("cls")

hit = abs(strength_user1 - strength_user2) + 1
counter = 1
while True:
  print("⚔️⚔️ -BATTLE TIME-  ⚔️⚔️")#2DO INICIO DE BATALLA
  print()
  print("The battle begins!")
  if health_user1 <= 0:
    print("Oh No!!! ", nameLegend_1, " the Mighty has died!")
    print(nameLegend_2, " the Almigthy destroyed ", nameLegend_1, " in the ", counter, "ª rounds!")
    break
    exit()
  elif health_user2 <= 0:
    print("Oh No!!! ", nameLegend_2, " the Mighty has died!")
    print(nameLegend_1, " the Almigthy destroyed ", nameLegend_2, " in the ", counter, "ª rounds!")
    break
    exit()
  else:
    user1_attack = dice6sided()
    user2_attack = dice6sided()
    if user1_attack > user2_attack:
      print(nameLegend_1," wins ", counter, "ª round")
      print(nameLegend_2, "takes a hit, with ", hit," damage")
      health_user2 -= hit
      print()
    elif user2_attack > user1_attack:
      print(nameLegend_2," wins ", counter, "ª round")
      print(nameLegend_1, "takes a hit, with ", hit," damage")
      health_user1 -= hit
      print()
    else:
      print("It's a tie")
    
    print("----------PLAYER 1----------")
    print("NickName   : ", nameLegend_1)
    print("Health     : ", health_user1)
    print("----------------------------")
    print()
    print("----------PLAYER 2----------")
    print("NickName   : ", nameLegend_2)
    print("Health     : ", health_user2)
    print("----------------------------")
    time.sleep(3)
    os.system("cls")
    counter += 1    
    continue
