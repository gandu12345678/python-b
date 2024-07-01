d={}
size=int(input("enter the number of persons:"))
for i in range(size):
    key = input("enter the email: ")
    value = input("enter the password:")
    d[key] = value

print("the dictionary is ",d)    
