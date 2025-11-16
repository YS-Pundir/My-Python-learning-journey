# property mehtod convert method to an attribute ,  and also it can change by making change in values of constructors
class Student:
    def __init__(self,phy,math,chem):
        self.phy=phy
        self.math=math
        self.chem=chem

    
    def percentage(self):
        return((self.phy+self.chem+self.math)/3)

student1 =Student(93,82,83)
print("the percentage of the student is",student1.percentage())

student1.math=99
print("updated percentage of the student is ",student1.percentage())
    