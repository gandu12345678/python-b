class Grandfather(object):
    house="big house"
    def __init__(self) -> None:
        print(self.house)
    
class Father(Grandfather):
    car="lamborghini"
    def __init__(self) -> None:
        print(self.car)
        super().__init__()

class Mother:
    jewelry="diamond"
    
 
class Son(Father,Mother):
    console="ps5"
    def __init__(self):
        print(self.console)
        super().__init__()
    

# father=Father()
# print("\n")
son=Son()
# print(son.jewelry)




