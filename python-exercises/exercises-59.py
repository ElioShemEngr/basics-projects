import datetime
'''
today = datetime.date.today()

print(today)

myDate = datetime.date(year=2024, month=3, day=26)

print(myDate)

difference = datetime.timedelta(days=365)

newDate = today + difference
print(newDate)
'''

print ("EVENT COUNTDOWN")
print()

day = int(input("Day:"))
month = int(input("Month:"))
year = int(input("Year:"))
eventDay = datetime.date(year, month, day)

print()
today = datetime.date.today()

if today > eventDay:
    print(f"This event was {today - eventDay} days ago 🥲🥲🥲")
elif today < eventDay:
    print(f"{eventDay - today} days left for this event 🕑⏰")
else:
    print("😄 Event is today 😄")

