# it means the --int--function
class Student:#Class
    def __init__(self,fullname,age):#making the constructors
        print("adding new  students to the database...")
        self.name=fullname#self is nothing but way to point the  the object of the class
        self.age=age
# objects
s1=Student("Yuvraj singh Pundir",19)
print(s1.name)
print(s1.age)

s2=Student("arpanjeet Singh",21)
print(s2.name)
print(s2.age)
# data that is stored in class is attributes
# def __intit__(self,all atributes.....)

# there are two types of constructers 1.defoult- with self parameter only 
# 2.parameetrized -which have the other paarmeters too