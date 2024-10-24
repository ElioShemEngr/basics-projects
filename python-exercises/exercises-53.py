import csv

with open("Day54Totals.csv") as file:
    reader = csv.DictReader(file)
    total = 0.0
    for row in reader:
        preview = float(row["Cost"]) * int(row["Quantity"])
        total += round(preview, 3)
        
    print(round(total,3))