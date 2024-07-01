class Person:
    
    def __init__(self,name,salary,password):
        self.name= name 
        self._salary=salary 
        self.__password=password
    
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,password):
        self.__password=password
        
    
ram=Person("ram",12,"123")
# ram.set_password("1234")
# print(ram.get_password())

ram.password="1234"
print(ram.password)