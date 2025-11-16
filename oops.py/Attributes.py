# Instance atributes - these are the attributes which have diffrent value for diffrent object 
# for example -names of student , such attributes we define by self._________ in constructors

# Class atrributes- the atrributes which have same value for same objects
# for example -college name for a student
# this will be written outside of the constructors
# we can access it by classname.________ in obejct


# class contains two things -- 1. Atrributes  2. Methods
# Methods are the functions inside the class

class Suv:#class
    Companyname="Mahindra"#Class attribute

    def __init__(self,name,model):#instance Attribute
        self.name=name
        self.model=model

    def Start(self):#method
        print("Wellcome to ",self.name)
        print("to start ",self.name,"please press the start button")
        print("your car's variaant is ",self.model)
# objects
car1=Suv("Mahindra Thar","Z Luxury")
print("Name of the manugacturer is ",Suv.Companyname)#for class attributes ,always write the clas name
print("the car name is ",car1.name)
print("the model of the car is ",car1.model)
car1.Start()
print("  ")

car2=Suv(" Mahindra XUV700","Z++")
print("the manufaccturer of the company is ",Suv.Companyname)
print("Name of the vahicle is ",car2.name)
print("Model of the car is ",car2.model)
car2.Start()#for calling the methods always use objects name not the class name