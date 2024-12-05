

def prime_num(num):

    is_prime=True

    for i in range(2,num):

        if num%i==0:

            is_prime=False

            break

    print( "Prime number"if is_prime==True else "Not prime")


prime_num(7)    
