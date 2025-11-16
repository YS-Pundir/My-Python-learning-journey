# static method is the method where we don't need to have self keyword , we can use it in every object
# when we use "@" in class it is called decorator
class result2:
    @staticmethod
    def greeetings():
        print("hello student \n")

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