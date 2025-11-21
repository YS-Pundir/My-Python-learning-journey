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

#function to find the maximum element in the list using for loop
def find_largest(numbers):
    max=numbers[0]
    for i in numbers:
        if i>max:
            max=i
    return max

#function to find minimum element in the list using for loop
def find_smallest(numbers):
    min=numbers[0]
    for i in numbers:
        if i<min:
            min=i
    return min

#function to display the results of all peroformed operations
def display_funciton():
    print("the sum of all elements in the list is :",compute_sum(length))
    print("the average of all elements in the list is :",compute_average(numbers))
    print("the largest element in the list is :",find_largest(numbers))
    print("the smallest element in the list is :",find_smallest(numbers))
    
display_funciton()