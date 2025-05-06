class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
         
e1 = Employee("Jack", 3455)
e2 = Employee("Jill", 3455)
print(Employee.company)         