import csv, os

with open("100MostSongs.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        artist = row['Artist(s)'].title()
        if artist in os.listdir():
            pass
        else:
            os.mkdir(artist)   
        song = row['Song']
        print(song)
        location = os.path.join(f"{artist}/", song)
        f = open(location, "w")
        f.close()
