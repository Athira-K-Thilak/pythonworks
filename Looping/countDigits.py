#count digits in a number

num=int(input("enter number:"))

count=0

i=1

while(num!=0):

    num=num//10

    count=count+1

print(count)    