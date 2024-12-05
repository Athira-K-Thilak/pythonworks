#Reverse a number using while loop

num=int(input("enter a number:"))

rev=0

while(num>0):

    last_digit=num%10

    rev=rev*10+last_digit

    num=num//10

print(rev)    