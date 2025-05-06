class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e = Employee("jack", 34555) 
e.projects = 6
print(e.projects)
