# super is used to use the attribtes and the method of the parent class 
# also the inheritence has its three type 1. single level 2. multi level 3. multi inheriteence

class Car:
    def __init__(self,type):
        self.type=type
      
    
    @staticmethod
    def started():
        print("first release the hand break\nthen press the start button")

    @staticmethod
    def stopped():
        print("to stop the car please put the hand break on\n and then use the key to switch the engine off")

class Toyota(Car):
    def __init__(self,name,model,type):#add the super atribute in inheritence's contructpr too
        self.name=name
        self.model=model
        super().__init__(type)
        super().started()
        super().stopped()

car1=Toyota("fortuner","Legender 2025","Suv")
print("the name of the car is ",car1.name)
print("the model of the car is ",car1.model)
print("the type of the vehivle is ",car1.type)