class Operation:

    def add(self,num1,num2):

        print(num1+num2)     

    def add(self,num1,num2,num3):

        print(num1+num2+num3) 


obj=Operation()

obj.add(10,20,40)


#no need to use method overloading as python is interpreted language and also we can use arguments to solve this

class Operation: 

    def add(self,*args):

        print(sum(args)) 


obj=Operation()

obj.add(10,20,40)
