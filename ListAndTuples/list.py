# lists  are muutable 
marks=[45,67,46,29,94,94,67]

print("the list is  -",marks)
print("the length of list is - ",len(marks))
print("the first element of list is -",marks[0])
print("the second element of list is -",marks[1])
print("the elements bitween firsst and fourth index is - ",marks[0:3])
marks[1]="kali"
print("the changed elements is-",marks[1])
# if we do not give the ending index then automatically it will be the ending index 
print("if we do not add end index then :",marks[1:])
# we can also do  the reverse slicing , but it starts with the negitive of 1 
print("reverse slicing -",marks[4:1])