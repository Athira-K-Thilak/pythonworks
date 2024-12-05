
class Employee:

    name:str
    id:int
    department:str
    salary:int

    def set_employee(self,name,id,department,salary):

        self.name=name
        self.id=id
        self.department=department
        self.salary=salary

    def dislpay(self):

        print(self.name,self.id,self.department,self.salary)

employee_instance1=Employee()

employee_instance2=Employee()

employee_instance1.set_employee("anamika",123,"developer",35000)

employee_instance2.set_employee("anju",124,"hr",30000)

employee_instance1.dislpay()

employee_instance2.dislpay()