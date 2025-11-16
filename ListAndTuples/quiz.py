arr=[1,2,3,4,5,6]
# printing the elements of the list
print("printing the elements of the list",arr[0:])
# inseritng the elements in the end
arr.insert(6,8)
print("the updaated array with the inserted element at the end is ->",arr)
# removing element at the specific index using the pop method
arr.pop(3)
print("the element at the 3rd index is removed->",arr)

# now we are diplaying the final array after appling all the operations
print(" the final array is ",arr[0:])