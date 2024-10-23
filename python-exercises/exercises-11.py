print("How many seconds in a year?")
print("---------------------------")
print()

# 60 seconds in 1 minute
minute = 60
# 60 minutes in 1 hour
hour = minute * 60
# 24 hours in 1 day
day = hour * 24

# Nota:
# Months are different lengths, you might need some math!
# Is it a leap year? +1 day!

yearType = input("Is it a leap year? > ")
if yearType == "yes":
    year = 366 * day
else:
    year = 365 * day

print(year)
