#Initialing list 
numbers=[]
length=int(input("enter the length of list", ))
if length>=2 and length <=10:
    for i in range(length):
      num=int(input("enter the number ",))
      numbers.append(num)

#function to find sum of all numbers in the list
def sum():
    s=0
    for i in numbers :
       s+=i
    return s


#funciton to find the average of every number  in the list
def average ():
   avg=sum()/length
   return avg


#function to find the maximum number in the list using for loop
def largest():
   max=numbers[0]
   for i in numbers:
      if i>max:
         max=i
   return max


#function to find the smallest element of the list
def smallest():
   min=numbers[0]
   for i in numbers:
      if i<min:
         min=i
   return min

#funciton to display the result of operation being done
def display():
   print("the list is ",numbers)
   print("the sum of eevry element of the list is ",sum())
   print("the average  of elements in the list is ",average())
   print("the larget number in the list is ",largest())
   print("the minimum element of the list is ",smallest())

display()
   

       