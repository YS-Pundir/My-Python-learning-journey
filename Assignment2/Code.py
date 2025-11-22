class NumberProcessor:
    def __init__(self,List):
        print("processing numbers ...")
        self.List=List
       
    
    # method to find sum of all elements in the  List
    def calculate_sum(self):
        sum=0
        for i in self.List:
            sum+=i
        return sum
    #method to caalculate average of all elements in the list
    def calculate_average(self):
        return self.calculate_sum()/len(self.List)
        

#taking input form user
list1=[]
for i in range(5):
    n=int(input("enter the number : ",))
    list1.append(n)
list1=NumberProcessor(list1)
print("the sum of all elements in the list is : ",list1.calculate_sum())
print("the average of all elements in the list is : ",list1.calculate_average())


    