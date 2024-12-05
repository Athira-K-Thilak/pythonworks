#check a number is palindrome or not by while loop

# num=int(input("enter a number:"))

# rev=0

# temp=num

# while(num!=0):

#     n=num%10

#     rev=rev*10+n

#     num=num//10

# if temp==rev:

#     print("palindrome")  

# else:

#     print("not a palindrome")      

number=int(input("enter a number:"))
original_number=number
reversed_number=0
is_palindrome=False
while(number>0):
    last_digit=number%10
    reversed_number=reversed_number*10+last_digit
    number=number//10
    if original_number==reversed_number:
        is_palindrome=True
print(is_palindrome)        