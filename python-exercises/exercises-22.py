def loginSystem():
    print("LOGIN SYSTEM")
    print()

    while True:
        username = input("Username > ").lower()
        password = input("Password > ").lower()
        print()

        if username == "elio" and password == "lolaso":
            print("Welcome to System")
            break
        else:
            print("Whoops! I don't recognise that username or password, try again...")
            print()
            continue

loginSystem()

