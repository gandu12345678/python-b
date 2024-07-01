database = []


def registration():

    name = input("enter your name:")
    email = input("enter your email:")
    password = input("enter your password:")

    database.append(
        {"name": name.lower(), "email": email.lower(), "password": password}
    )

    if database.__len__() == 1:
        print("You have successfully registered")
    else:
        print("you arent registered yet")


def login(database):
    email = input("enter your email:")
    password = input("enter your password:")
    for userdata in database:
        if (userdata["email"] == email.lower()) and (userdata["password"] == password):
            print("\n")
            print("you are logged in ")
            print("\n")

            print(f"your database values are :{database}")
            print("\n")
        else:
            print("wrong cridentials")


def main():
    while True:
        print("\n=== To-do list ===")
        print("1> register your id")
        print("2> login")
        print("3> quit")

        choice = int(input("enter your choice:"))
        if choice == 1:
            registration()
        elif choice == 2:
            login(database)
        elif choice == 3:
            print("thank you for operating this to_do list")
            break
        else:
            print("invalid choice.please try again")


if __name__ == "__main__":
    main()
