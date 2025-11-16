# 1.Abstraction-->hiding the implementation details of a class and only showing the essential feature to user
#  2.encapsulation-->Wrapping the data in a single unit(object)
class Account:
    def __init__(self,balance,accnumber,__accountPass):
        self.password=__accountPass
        self.balance=balance
        self.accnumber=accnumber

    def resetPass(self,newPass):

        newPass=int(input("Enter your new password ",))
        __accountPass=newPass#making the attribute private by double slash
        print("your new password ",newPass,"has been rested successfully")

    def debit(self,amount):
        self.balance-=amount
        print("the amount of ",amount," is debited from your account ",self.accnumber," the remaining balance is ",self.balance)
    
    def credit(self,amount):
        self.balance+=amount
        print("the amount of ",amount," has been credited to your account ",self.accnumber," the current balance is ",self.balance)

customer=Account(10000000,123456667)
customer.debit(30000)
customer.credit(40000)


