#creating class 
class Marks_sheet:
    def __init__(self,Subject,Assignment_marks,Quize_marks,Final_marks):
        self.Subject=Subject
        self.Assignment_marks=Assignment_marks
        self.Quize_marks=Quize_marks
        self.Final_marks=Final_marks
    def sum(self):
        return self.Assignment_marks+self.Final_marks+self.Quize_marks

   
Subject1=Marks_sheet("maths",15,18,19)
print("the total marks obtained by student in Maths is :",Subject1.sum())
subject2=Marks_sheet("physics",14,19,20)
print("the total marks obtained by student in Physics : ",subject2.sum())
subject3=Marks_sheet("chemistry",19,20,22)
print("the total marks obtained by student in chemistry is :",subject3.sum())
subject4=Marks_sheet("English",17,18,19)
print("the total marks obtained by student in English ",subject4.sum())
subject5=Marks_sheet("Physical Education",20,19,19)
print(("the total marks obtained by student in Physical Education is : ",subject5.sum()))

        
    

    
    


    



