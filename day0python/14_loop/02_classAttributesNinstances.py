class  Employee:
    def _init_(self, salary, name, bond):

        self.salary = salary
        self.name = name 
        self.bond = bond
    def get_salary(self):
        return self.salary
    

e1 = Employee(34000, "john Doe", 4)

print(e1.get_salary())