print("WebPage Information")
print()

webPage = {"name" : None, "url" : None, "desc" : None, "rating" : None}

for key, value in webPage.items():
    webPage[key] = input(f"{key} : ")

print()

for key, value in webPage.items():
    print(f"{key} : {value}")
