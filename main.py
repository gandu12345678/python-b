# from filehandling import sum
# from funution import sum as multi

# sum(1,2,3)


while True:
    try:
        first_number=int(input("first number:"))
        second_number=int(input("second number:"))
        print(first_number/ second_number)
    
    except ZeroDivisionError:
        print("you cant divide by zero")
    
    except ValueError:
        print("wrong value inputed")
    
    except Exception as e:
        print(e)