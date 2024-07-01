from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self,app):
        pass
    def run(self,app):
        self.process(app)
    
class Laptop(Computer):
    def process(self,app):
        print(f"laptop is running {app}")

class Mobile(Computer):
    def process(self,app):
        print(f"mobile is running {app}")

dell=Laptop()
dell.run("pubg")

samsung=Mobile()
samsung.run("pubg")
        