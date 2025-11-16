# dictionary are stored in key:value pair
# they are unorderd and , mutable ,do not allow any duplicate key
info={
    "name":"Yuvraj Singh Pundir",
    "proffession ":"Student",
    "Study":"Software engineering",
    "Subjects":("english","programing","maths","software development"),
    "Grades":[99,69,98,67]

}
print("this is our current dictionary->",info)
print("Now i am tring to  print an key of this dictionary->",info["Subjects"])

# assigning the diffrent value to the key
info["name"]="mehak dhull"
print(info)

# nested dictionary
student={
    "name":"Yuvarj  Singh Pundir",
    "Subjects":{
        "maths":90,
        "physics":100,
        "chemistry":89
            },

    "crushes":"none",
    "GF":"aukat se bahar"

            
}

print(student["Subjects"]["chemistry"])
# way to print all keys
print(student.keys()," these are the all keys that  are in this dicht")
# way to wrriet the value of the ditionaries
print(student.values())
# to  return the key value of the key and the values in form of tuples
print(student.items())
# wway  to access it one by one , first we always have to convert it to the list , because we tuples are immutable
pair=list(student.items())

print(pair[0])
# to  get any value from a key
print(student.get("Subjects"))

new_dict={"time":"quite good","mood":"nervous"}
student.update(new_dict)
print("this is the updated dictionary->",student)
