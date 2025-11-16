# polymorphisam - when same operater have diffrent meaning according to the ocntext , that means polymorphysism
# for exmaple - complex number is part of both real part an imaginary part
# as we know that there are no concept of cmplex number in python , so we will do it for that example 
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i + ",self.img,"j")

    def __add__(self,num2):
        newReal=num1.real+num2.real
        newimg=num1.img+num2.img
        return Complex(newReal,newimg)#returning class with newreal and new imaginary number
    
    def __sub__(self,num2):
        newReal=num1.real-num2.real
        newimg=num1.img-num2.img
        return Complex(newReal,newimg)
    
    def __mul__(self,num2):
        newReal=num1.real*num2.real
        newimg=num1.img*num2.img
        return Complex(newReal,newimg)
    
    # for division -- __truediv__
    # for reminder- a__mod__b
        

num1=Complex(3,4)
num1.showNumber()

num2=Complex(5,6)
num2.showNumber()

addition=num1+num2
addition.showNumber()

substraction=num1-num2
substraction.showNumber()

product=num1*num2
product.showNumber()
 