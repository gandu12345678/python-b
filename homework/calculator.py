a=input("enter a arithmetic operator:")
b=int(input("enter a number:"))
c=int(input("enter another number:"))
d=b+c
e=b-c
f=b*c
g=b/c
h=b%c
i=b**c
if a== "+" or a=="add" or a=="sum":
    print("the sum of the numbers is",d)
    
elif a=="-" or a=="minus" or a=="substract":
    print("the difference between the numbers is",e)
    
elif a=="*" or a=="multiplication":
    print("the multiplication of the numbers is",f)
    
elif a=="/" or a=="divison" or a=="divide":
    print("the difference between the numbers is",g)
    
elif a=="%" or a=="modulus":
    print("the modulus of the numbers is",h)

elif a=="**" or a=="power":
    print("the modulus of the numbers is",i)
    
else:
    print("WRONG OPERATOR")
