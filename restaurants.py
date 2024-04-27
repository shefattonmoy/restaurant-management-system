from menus import Menu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)
    
    def view_employees(self):
        print("*****Employee List*****")
        for emp in self.employees:
            print(emp.name, emp.phone, emp.email, emp.address)