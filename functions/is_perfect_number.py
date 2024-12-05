

def is_perfect_number(number):

    total=0

    for i in range(1,number):

        if number%i==0:

            total=total+i

    print("Perfect" if total==number  else "Not Perfect")

is_perfect_number(5)        