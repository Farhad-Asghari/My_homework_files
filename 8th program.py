# Creat a class Employee with attributes name and salary. Creat a derived class Mananger with an additional attribute department.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary,)
        self.department = department
new_employee = Employee("Farhad", 20000)
our_manager = Manager("reza", 10000, "IT")
print(our_manager.department)