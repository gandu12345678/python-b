import os


def createFile():
    filename = input("Enter a filename with extension: ")
    if os.path.exists(filename):
        print("\n")

        print("The filename already exists")

        print("\n")

    else:
        print(filename)
        f = open(filename, "x")

        print(f"file has been successfully created! Your file name is :  {filename}")


def write():
    filename = input("enter the filename where you want to write text : ")
    try:
        f = open(filename, "w")
        content = input("enter the content text : ")
        f.write(content)
        f.close()
        print(f"content is added into your file : {content}")

    except Exception as e:
        print(f"error while writing text to file {e}")


def Append():
    filename = input("enter the filename  ")
    try:
        f = open(filename, "a")
        content = input("enter the text to append  : ")
        f.write(content)
        f.close()
        print("the changes have been made!")

    except Exception as e:
        print(f"error while appending text into a file {e}")


def delete():
    filename = input("Enter the filename to delete: ")
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(
                "The file does not exist \n Please enter the valid filename: "
            )
        os.remove(filename)
        print("The file is deleted successfully")

    except Exception as filenotFound:
        print(filenotFound)

    except Exception as e:
        print("error deleting file : ")


def read():
    try:
        filename = input("enter the filename to read : ")
        if not os.path.exists(filename):
            raise FileNotFoundError(
                "file not found please enter valid filename to read :)"
            )
        f = open(filename, "r")
        print(f.read())

    except Exception as filenotfound:

        print(filenotfound)


def main():
    while True:
        print("\n ==file handling==")
        print("1> create a file")
        print("2> read a file")
        print("3> write on the file")
        print("4> append the file")
        print("5> delete any files")
        print("6> quit")

        choice = int(input("enter your choice:"))
        if choice == 1:
            createFile()
        if choice == 2:
            read()
        elif choice == 3:
            write()
        elif choice == 4:
            Append()

        elif choice == 5:
            delete()
        elif choice == 6:
            print("thank you for operating this app")
            break
        else:
            print("invalid choice.please try again")


if __name__ == "__main__":
    main()
