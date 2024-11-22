print("How many seconds in a year?")
print("---------------------------")
print()

# 60 seconds in 1 minute
minute: int = 60
# 60 minutes in 1 hour
hour: int = minute * 60
# 24 hours in 1 day
day: int = hour * 24

# Nota:
# Months are different lengths, you might need some math!
# Is it a leap year? +1 day!

yearType: str = input("Is it a leap year? > ")
if yearType == "yes":
    year = 366 * day
else:
    year = 365 * day

print(year)
