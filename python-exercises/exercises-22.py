def loginSystem():
    print("LOGIN SYSTEM")
    print()

    while True:
        username = input("Username > ")
        password = input("Password > ")
        print()

        if username == "elio" and password == "lolaso":
            print("Welcome to System")
            break
        else:
            print("Whoops! I don't recognise that username or password, try again...")
            print()
            continue

loginSystem()

