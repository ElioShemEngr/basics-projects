print("WebPage Information")
print()

webPage = {"name" : None, "url" : None, "desc" : None, "rating" : None}

nameWeb = input("name : ")
urlWeb = input("url : ")
descWeb = input("desc : ")
ratingWeb = input("rating : ")

webPage["name"] = nameWeb
webPage["url"] = urlWeb
webPage["desc"] = descWeb
webPage["rating"] = ratingWeb

print()

for key, value in webPage.items():
    print(f"{key} : {value}")

