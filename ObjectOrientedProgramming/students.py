
class Student:

    name:str

    rollnumber:int

    age:int

    course:str

    def set_student(self,name,rollnumber,age,course):

        self.name=name
        self.rollnumber=rollnumber
        self.age=age
        self.course=course
    def display(self):

        print(self.name,self.rollnumber,self.age,self.course)

student_instance1=Student()
student_instance2=Student()
student_instance1.set_student("anju",2,23,"b.tech")
student_instance2.set_student("anu",3,24,"software development")
student_instance1.display()
student_instance2.display()           