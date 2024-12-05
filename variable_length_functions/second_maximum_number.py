def second_largest(*args):

    sorted_numbers=sorted(args,reverse=True)  

    return sorted_numbers[1]

print(second_largest(10,30,20))
print(second_largest(10,5,6,34,56,90,23,45,78))


# kwargs

def display_mobile_data(**kwargs):

    print(kwargs.get("name"))

    print(kwargs.get("price"))

display_mobile_data(name="oneplus",price=32000,display="amoled")


#calculator(10,20,30,operation="+")

#calculator(10,11,12,)

def calculator(*args,**kwargs):

    if kwargs.get("operation")=="+":

        return sum(args)
    
    if kwargs.get("operation")=="*":
        result=1

        for num in args:

            result=result*num

        return result

print(calculator(10,20,30,operation="+"))        