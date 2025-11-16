# creating the class for name and marks of 3 subjects and a method to print the average
class result:
    def __init__(self,name,maths,physics,chemistry):
        self.name=name
        self.Maths=maths#take care of capitalisation of words
        self.physics=physics
        self.chemistry=chemistry

    def average(self):
        ave=(self.Maths+self.chemistry+self.physics)/3
        return ave
    
student1=result("Yuvraj Singh Pundir",93,82,83)
print("the result of ",student1.name," maths-> ",student1.Maths,"\n physics->",student1.physics,"\nChemistry->",student1.chemistry)
print("the average of marks is >",student1.average())

# we can also do this by loop method
class result2:
    def __init__ (self,name,marks):
        self.name=name
        self.marks=marks
    
    def average2(self):
        sum=0
        for value in self.marks:
            sum+=value
        print("hi ",self.name," your avg marks are ",sum/3)

student2=result2("Yuvraj Singh Pundir",[93,83,82])
student2.average2()
    

    