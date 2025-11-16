# defination of call 
def cal_sum(a,b):
    sum=a+b
    print(sum)
    return sum

# funtion call

cal_sum(1,2)
# second call
cal_sum(2,10)

# another example
def cal_sum(a,b):
    return a+b

sum=cal_sum(3,5)
print(sum)

# another example for calculating average of any amount of numbers  numbers

def average(list):
    return ( sum(list))/len(list)




list=[]

x=int(input("enter the first number here ",))
list.append(x)
y=int(input("enter the second number ",))
list.append(y)
z=int(input("enter the third number",))
list.append(z)
a=int(input("enter the fourth number ",))
list.append(a)

av=average(list)

print(av)
 

# print the length of the function
def length(list):
    return len(length)

list=[1,2,3,4,5,6,7]
lenList=len(list)
print(lenList)

# pritnting  the elemeents of the list in a straight line
def el(list,x):
    return list[x]

list=[1,2,3,4,5,6,7,8]
print(list)
for item in list:
    print(item,end=" ")

# function of factorial of n 


def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

cal_fact(5)

# cconverting  inr to usd
def dollar(ruppee):
    return ruppee*83

r=45
print(dollar(r))




