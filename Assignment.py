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

#function to find the 