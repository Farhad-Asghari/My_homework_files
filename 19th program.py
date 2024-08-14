# Creat a class Company with attributes name and employees(a list of Embloyee objects). Provide methods to add an remove employees.
class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []
        
    def add_employee(self,employee):
        self.employees.append(employee)
        print(f"{employee.name} is added in {self.name} company")
        
    def remove_employee(self, employee_name):
        for employee in self.employees:
            if employee.name == employee_name:
                print(f"{employee_name} is deleted from {self.name} company")
                return print(f"{employee_name} is not found in {self.name} company")
company1 = Company("apple")
employee1 = Employee("Alison")
employee2 = Employee("Jack")
company1.add_employee(employee1)
company1.add_employee(employee2)
company1.remove_employee("Alison")