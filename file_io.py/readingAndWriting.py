# this mode helps  us to read as well as write without truncating
#  , it means the past content of the  file will not be  erased
# and also  one thing is that the new content will be written in the starting
f=open("ram.txt","r+")
print(f.read())
f.write("abc")
f.close()
# this mode helps us to open file to read and write , while the content is  truckated
w=open("ram.txt","w")
print(w.read())
print(w.write("abc"))
