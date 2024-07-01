# class House:
#     door=10
#     window=5
#     color="red"
    
#     def __init__(self, door,window,color):
#         self.door=door
#         self.window=window
#         self.color=color
#     def __str__(self):
#         return self.color
        
# ram_ko_ghar=House(door=2,window=1,color="green")
# # print(ram_ko_ghar.color)

# print(ram_ko_ghar)

class Employee:
    
    def __init__(self,name,age,salary):
        self.name = name
        self.age=age
        self.salary=salary
    def __le__(self,object):
        return self.age== object.age
    
        
ram = Employee("ram",22,2000)
shyam=Employee("shyam",22,2200)

print(ram<=shyam)

