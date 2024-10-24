#Esto pertenece al cap. 31 del curso de Replit
def changeColor(color):
    if color=="white":
        return("\033[37m")
    elif color=="cyan":
        return("\033[36m")
    elif color=="purple":
        return("\033[35m")
    elif color=="blue":
        return("\033[34m")
    elif color=="yellow":
        return("\033[33m")
    elif color=="green":
        return("\033[32m")
    elif color=="red":
        return("\033[31m")
    elif color=="black":
        return("\033[30m")
    else:
        return("\033[0m")


title = f"{changeColor('red')}={changeColor('white')}={changeColor('blue')}={changeColor('yellow')}MusicPlayer{changeColor('blue')}={changeColor('white')}={changeColor('red')}="

print(f"           {title:^50}")
print()
print(f"🔥▶️ {changeColor('white')}Radio Gaga")
print(f"\t{changeColor('yellow')}Queen")
print()

prev = f"{changeColor('white')}PREV"
next = f"{changeColor('green')}NEXT"
paus = f"{changeColor('red')}PAUSE"

print(f"{prev:<45}")
print(f"{next:^45}")
print(f"{paus:>45}")

print()
print()
print()

title2 = f"{changeColor('white')}WELCOME TO"
subtitle2 = f"{changeColor('blue')}--  ARMBOOK   --"

print(f"{title2:^45}")
print(f"{subtitle2:^45}")
print()

text1 = f"{changeColor('yellow')}Definitely not a rip off of"
text2 = f"{changeColor('yellow')}a certain other social"
text3 = f"{changeColor('yellow')}networking site."

print(f"{text1:>45}")
print(f"{text2:>45}")
print(f"{text3:>45}")
print()

honest = f"{changeColor('red')}Honest."

print(f"{honest:^45}")
print()

username = f"{changeColor('white')}Username: "
password = f"{changeColor('white')}Password: "

print(f"{username:^45}")
print(f"{password:^45}")
print()