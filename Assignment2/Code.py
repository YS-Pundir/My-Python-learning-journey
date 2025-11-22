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
    #method to find largest element in the list
    def find_largest(self):
        max=self.List[0]
        for i in self.List:
            if i>max:
                max=i
        return max
    #method to find smallest element in the List
    def find_smallest(self):
        min=self.List[0]
        for i in self.List:
            if i <min:
                min=i
        return min
    #method to diplay all thhe  results
    def display_results(self):
        print("the sum of all elements in the list is : ",self.calculate_sum())
        print("the average of all elements in the list is : ",self.calculate_average())
        print("the largest element in the list is : ",self.find_largest())
        print("the smallest element in the list is : ",self.find_smallest())
        

#taking input form user
list1=[]
for i in range(5):
    n=int(input("enter the number : ",))
    list1.append(n)
list1=NumberProcessor(list1)
list1.display_results()



    