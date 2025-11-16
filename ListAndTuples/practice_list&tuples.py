movies=[]

movie1=input("enter the 1st movie name", )
movie2=input("enter the 2nd movie name", )
movie3=input("enter the 3rd movie name", )

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)

movies.append(input("enter the first movie",))
movies.append(input("enter the second movie ",))
movies.append(input('enter the  third movie'))
print(movies)



# checking if thee list is pelimdrome or not 
list1=[1,2,3,2,1]
list2=[1,2,3,4,5]

copy_list1=list1.copy

if(list1==copy_list1):
    print("the list 1 is peledrome")
else:
    print("the list is not  pelidrome")

# checkign for list2
copy_list2=list2.copy

if(copy_list2==list2):
    print("the list 2 is also pelidrome  ")
else:
    print("the list number  two is not pelidrome")

# cheking how many students have scored a 
grades=["C","D","A","A","B","B","A"]

student =grades.count("A")
print("number fo student with A grade is  ->",student)