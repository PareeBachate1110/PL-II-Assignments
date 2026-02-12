class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def d1(self):
        print("Name (Person) :",self.name)
        print("Age (Person) :",self.age)
        print("--------------------------------------------------")
        

class Employee(Person):
    def __init__(self,name,age,emp_id,salary):
        Person.__init__(self,name,age)
        self.emp_id=emp_id
        self.salary=salary

    def d2(self):
        print("Name (Employee) :",self.name)
        print("Age (Employee) :",self.age)
        print("Employee ID (Employee) :",self.emp_id)
        print("Salary (Employee) :",self.salary)
        print("--------------------------------------------------")

class Manager(Employee):
    def __init__(self,name,age,emp_id,salary,dept):
        Employee.__init__(self,name,age,emp_id,salary)
        self.dept=dept

    def d3(self):
        print("Name (Manager) :",self.name)
        print("Age (Manager) :",self.age)
        print("Employee ID (Manager) :",self.emp_id)
        print("Salary (Manager) :",self.salary)
        print("Department (Manager) :",self.dept)
        print("--------------------------------------------------")

e1=Manager("Anil","32","ABC0001","50000","Marketing")
e1.d3()
e2=Person("Reshma","27")
e2.d1()
e3=Employee("Sania","40","ABC0003","100000")
e3.d2()