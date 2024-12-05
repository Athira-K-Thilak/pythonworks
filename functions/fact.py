

def factorial(num):

    fact=1

    # while(num!=0):
        
    #     i=num

    #     fact=fact*i

    #     num=num-1

    # fact=1

    for i in range(1,num+1):

        fact=fact*i

    # print(fact)    

    return fact

result=factorial(3)    

print(result)