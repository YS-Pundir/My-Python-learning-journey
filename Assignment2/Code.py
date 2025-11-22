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


    