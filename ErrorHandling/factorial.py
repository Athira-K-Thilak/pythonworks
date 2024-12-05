

def factorial(number):

    fact=1
    

    while(number>0):

        fact=fact*number

        number=number-1

        return fact
    

def factorial_check():

    assert factorial(0)==1,"factorial chk passed"

    assert factorial(2)==4,"factorial chk passed"

    assert factorial(-1)



        