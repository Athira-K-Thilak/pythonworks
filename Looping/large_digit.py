
num=int(input('enter a number:'))

max=0

while(num>0):

    digit=num%10

    if max<digit:

        max=digit

    num=num//10
    

print("large digit is",max)        
