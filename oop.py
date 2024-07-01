# class House:
#     door =10
#     window=5
#     color="red"
    
#     def set_color(self,color):
#         self.color=color
    
#     def get_color(self):
#         return self.color
        

# ram_ko_ghar=House()
# shyam_ko_ghar=House()

# print(ram_ko_ghar.get_color())

# ram_ko_ghar.set_color("green")
# print(ram_ko_ghar.get_color())

class Burger:
    
    def patty(self):
        print("patty")
        return self
    def sauce(self):
        print("sauce")
        return self
    def saag(self):
        print("saag")
        return self
    def bun(self):
        print("bun")
        return self
burger=Burger()

burger.bun() \
    .sauce() \
    .patty() \
    .saag() \
    .sauce() \
    .bun()