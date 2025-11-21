numbers=[]
length=len(numbers)
length=int(input("enter the length of the list: ",))

def create_list():#function to create a list
    if length>=2 and length<=10:#as requirement : length should be bitween 2 and 10
        for i in range(length):
            el=int(input("enter the element :",))
            numbers.append(el)
    else:
        print("length should be bitween 2 and 10 ")

create_list()
print("the created list is :",numbers)

#function to find the sum of all elements in the list
def compute_sum(numbers):
    sum=0
    for i in range (numbers):
        sum+=i
    return sum

#function to find the average of all elements in the list
def compute_average(numbers):
    avg=compute_sum(numbers)/length
    return avg
