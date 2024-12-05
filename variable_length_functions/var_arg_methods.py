

# def add_numbers(*args):# this accept any number of arguments as tuple

#     print(args)

# add_numbers(10,20)
# add_numbers(10,20,30)

def products(*args):

    result=1

    for num in args:

        result=result*num

    return result

print(products(10,20))    
print(products(10,20,5,6))   

# def sum_num(*args):

#     return sum(args)

# print(sum_num(10,20,30))        