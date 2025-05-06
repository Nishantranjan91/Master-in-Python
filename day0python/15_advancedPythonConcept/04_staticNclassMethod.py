class Employee:
    
    def print_info(self):
    info = f"The name is {self.name}and the salary is {self.salary}"
    print(info)
e1 = Employee("Jack",3455)
e2 = Employee("Jill", 3455) 
e1.print_info()     