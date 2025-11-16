# # if we want to change the class attribute using the method 
# class person:
#     name="Prashant"
#     def changename(self,name):
#         person.name=name
   

# man=person()
# print(person.name)
# print(man.name)

# but doing same thing with class method
class person2:
    name="Singh"

    # def changename(self,name):
    #     self.__class__.name="Pundir"
    @classmethod
    def changename(abc,name):
        abc.name=name


man2=person2()
person2.changename("Yuvraj Singh Pundir")
print(man2.name)
print(person2.name)

# class method is bound to the class & receives the class as an implicite first argument
# threee types of method 1. static meethod 2. class method 3. instance method