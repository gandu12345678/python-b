""" def sum(*numbers):#args-->> arugements
    total=0
    for number in numbers:
        total+=number
    print (total)
sum(1,2,3) """

# def person(**kwargs):
#     print(kwargs["name"],kwargs["age"],kwargs["gender"],kwargs["birth"])
# person(name="ram",age="22",gender="male",birth="2000/01/01")

def sum(a,b):
    return a+b
sum_of=sum(1,2)
print(sum_of)


# def number(n):
#     print(n)
#     if n==10:
#         return
#     number(n+1)
    
# number(1)
