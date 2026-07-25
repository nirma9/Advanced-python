class employee:
               def __init__(self,name,salary):
                       self.name = name
                       self.salary = salary
               def display_details(self):
                       print(f"Nmae: {self.name} , salary : {self.salary}")
emp1 = employee("riya",500000)
emp1.display_details()