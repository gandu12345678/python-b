
def registration():
    database=[]
    name=input("enter your name:")
    email=input("enter your email:")
    password=input("enter your password:")
    
    database.append(
        {
            "name":name.lower(),
            "email":email.lower(),
            "password":password
            
        }
    )
    
    if(database.__len__()==1):
        print("You have successfully registered")
        print("now you will be directed towards the login page")
        
        login(database)
    else:
        print("you arent registered yet")

def login(database):
    email=input("enter your email:")
    password=input("enter your password:")
    for userdata in database:
        if((userdata["email"]==email.lower()) and (userdata['password']==password)):
             print("\n")
             print("you are logged in ")
        
             print(f"your database values are :{database}")
             print("\n")
        
        
    
    else:
        print("your email or password doesnot match")
    
    


registration()
    
    