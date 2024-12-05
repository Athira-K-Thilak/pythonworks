
number=int(input("enter a number:"))

total=0

while(number>0):

    last_digit=number%10

    digit_square=last_digit**2

    total=total+last_digit**2

    number=number//10

print(total)    

