numbers = []
length = int(input("enter the length of the list: "))

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
def compute_sum(nums):
    total = 0
    for i in nums:
        total += i
    return total

#function to find the average of all elements in the list
def compute_average(nums):
    if len(nums) == 0:
        return 0
    return compute_sum(nums) / len(nums)

#function to find the maximum element in the list using for loop
def find_largest(nums):
    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    return largest

#function to find minimum element in the list using for loop
def find_smallest(nums):
    smallest = nums[0]
    for i in nums:
        if i < smallest:
            smallest = i
    return smallest

#function to display the results of all peroformed operations
def display_function():
    print("the sum of all elements in the list is :", compute_sum(numbers))
    print("the average of all elements in the list is :", compute_average(numbers))
    print("the largest element in the list is :", find_largest(numbers))
    print("the smallest element in the list is :", find_smallest(numbers))

display_function()