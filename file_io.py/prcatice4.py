# in file enter the file to enter the numbers separated by comas and count he even numbers
with open("sample.txt","r") as f:
    data=f.read()
    print(data)#first take each number out and then caste them into integer value

    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(num)
            num=""
        else:
            num+=data[i]
# another way of doing this
count=0
with open("sample.txt","r") as f:
    data=f.read()
    print(data)

    nums=data.split(",")
    for value in nums:
        if(int(value)%2==0):
            count+=1
print(count)

