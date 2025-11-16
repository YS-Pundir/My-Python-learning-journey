class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        
        print("the employee is an  ",self.role)
        print("His Salary per month is ",self.salary)
        print("His department  is ",self.dept)

class Engineer(Employee):
    def __init__(self,role,dept,salary,name,age):
        self.name=name
        self.age=age
        super().__init__(role,dept,salary)
        

emp1=Engineer( "Coder","Production","700000","Prashant Jhangra",22)
emp1.showDetails()

    