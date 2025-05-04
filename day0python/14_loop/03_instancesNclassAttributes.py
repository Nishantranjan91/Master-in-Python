class  Employee:
    company = "Asus"
    def _init_(self, salary, name, bond):

        self.salary = salary
        self.name = name 
        self.bond = bond
    def get_salary(self):
        return self.salary
    
    def get_salary(self):
        print(f"the name of the employee is {self.name}.Salary is {self.salary}.the bond is for {self.bond} years")
    
e1 = Employee(34000, "john", 3)
print(e1.company)