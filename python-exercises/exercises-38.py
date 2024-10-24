import os, time, random

print("Play Game Hangman!")

listCountries = ["Afghanistan","Albania","Algeria",
"Andorra","Angola","Anguilla",
"Antigua and Barbuda",
"Argentina","Armenia",
"Aruba","Australia","Austria",
"Azerbaijan","Bahamas","Bahrain",
"Bangladesh","Barbados","Belarus",
"Belgium","Belize","Benin","Bermuda",
"Bhutan","Bolivia","Bosnia & Herzegovina",
"Botswana","Brazil","British Virgin Islands",
"Brunei","Bulgaria","Burkina Faso","Burundi",
"Cambodia","Cameroon","Cape Verde",
"Cayman Islands","Chad","Chile","China",
"Colombia","Congo","Cook Islands",
"Costa Rica","Cote D Ivoire","Croatia",
"Cruise Ship","Cuba","Cyprus","Czech Republic",
"Denmark","Djibouti","Dominica",
"Dominican Republic","Ecuador","Egypt",
"El Salvador","Equatorial Guinea",
"Estonia","Ethiopia","Falkland Islands",
"Faroe Islands","Fiji","Finland","France",
"French Polynesia","French West Indies","Gabon",
"Gambia","Georgia","Germany","Ghana","Gibraltar",
"Greece","Greenland","Grenada","Guam","Guatemala",
"Guernsey","Guinea","Guinea Bissau","Guyana",
"Haiti","Honduras","Hong Kong","Hungary","Iceland",
"India","Indonesia","Iran","Iraq","Ireland",
"Isle of Man","Israel","Italy","Jamaica","Japan",
"Jersey","Jordan","Kazakhstan","Kenya","Kuwait",
"Kyrgyz Republic","Laos","Latvia","Lebanon",
"Lesotho","Liberia","Libya","Liechtenstein",
"Lithuania","Luxembourg","Macau","Macedonia",
"Madagascar","Malawi","Malaysia","Maldives",
"Mali","Malta","Mauritania","Mauritius","Mexico",
"Moldova","Monaco","Mongolia","Montenegro",
"Montserrat","Morocco","Mozambique","Namibia",
"Nepal","Netherlands","Netherlands Antilles",
"New Caledonia","New Zealand","Nicaragua","Niger",
"Nigeria","Norway","Oman","Pakistan","Palestine",
"Panama","Papua New Guinea","Paraguay","Peru",
"Philippines","Poland","Portugal","Puerto Rico",
"Qatar","Reunion","Romania","Russia","Rwanda",
"Saint Pierre & Miquelon","Samoa","San Marino",
"Satellite","Saudi Arabia","Senegal","Serbia",
"Seychelles","Sierra Leone","Singapore","Slovakia",
"Slovenia","South Africa","South Korea","Spain",
"Sri Lanka","St Kitts & Nevis","St Lucia",
"St Vincent","St. Lucia","Sudan","Suriname","Swaziland",
"Sweden","Switzerland","Syria","Taiwan","Tajikistan",
"Tanzania","Thailand","Timor L'Este","Togo","Tonga",
"Trinidad & Tobago","Tunisia","Turkey","Turkmenistan",
"Turks & Caicos","Uganda","Ukraine",
"United Arab Emirates","United Kingdom","Uruguay",
"Uzbekistan","Venezuela","Vietnam",
"Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]


country = random.choice(listCountries)
listLetters = []
vidas = 6
figAhorcado = 1

# Figuras de ahoracado en ASCII sacado de replit
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Titulo del juego ahorcado
print("----------------------------")
print("⚔️☠️JUEGO DEL AHORACADO☠️⚔️")
print("----------------------------")
print()

# Imprimir palabra al azar y los espacios que requiere
print(country)

for i in country:
    print("_", end="")
print()


# Ciclo para desarrollo de adivinanza
while True:
    print()
    letter = input("Enter a letter -> ")

    if letter in listLetters:#verifica si la letra ya fue introducida
        print("La letra ya fue introducida...")
        continue
    
    listLetters.append(letter)#Agrega una letra a la lista de letras
    
    if letter in country:#verifica si la letra esta en la palabra
        print("La letra es correcta")
        print()
    else:
        print("La letra es incorrecta")
        vidas -= 1
        print(HANGMANPICS[figAhorcado])
        print(f"Te quedan {vidas} vidas")
        figAhorcado += 1

    if vidas == 0:#Verifica si aun le quedan vidas
        print("Ha perdido el juego")
        print()
        break
    
    allLetters = True#Verifica las letras encontradas y faltantes
    for i in country:
        if i in listLetters:
            print(i, end="")
        else:
            print("_", end="")
            allLetters = False
    print()

    if allLetters: #Verifica que todas las letras esten completas
        print(f"Has ganado con {vidas} vidas")
        break
    
    if vidas == 0:#Verifica si aun le quedan vidas
        print("Ha perdido el juego")
        print()
        break

'''
select = random.choice(listCountries)

print("")
print(select)
print("")

for i in select:
    print("_", end = '')
print("")

userLetter = input("In letter choice > ")

for i in select:
    if i == userLetter:
        print(userLetter, end = '')
    else:
        print("_", end = '')

if userLetter in select:
    print("Yes letter in word!!!")
else:
    print("Nop letter in word")

'''