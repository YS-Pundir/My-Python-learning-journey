with open("practice.txt","w") as f:
    f.write("Hi everyone \nwe are learning File I/O\nusing Java\nI like programming in Java")
# writing the function to replace every occurance of java with python
#  first we will read our file and then we can overwrite it 
with open("practice.txt","r") as f:
    data=f.read()
    new_data=data.replace("Java","Python")
    print(new_data)
    
# now we have replacd that in the resding of the file 
# ,but it is not being replaced in the actual file so we have to rewrite it
with open("practice.txt","w") as f:
    f.write(new_data)# now it is done
