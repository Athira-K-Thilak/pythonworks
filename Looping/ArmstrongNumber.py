

# number=int(input("enter number:"))

# digit_count=len(str(number))

# original=number

# total=0

# while(number>0):

#     digit=number%10

#     exponent=digit**digit_count

#     total=total+exponent

#     number=number//10

# print("Armstrong number" if original==total else "Not Armstrong number")

number=int(input("enter a number"))
original_number=number
digit_count=len(str(number))
sum=0
is_armstrong=False
while(number>0):
    digit=number%10
    exponent=digit**digit_count
    sum=sum+exponent
    number=number//10
    if original_number==sum:
        is_armstrong=True
print(is_armstrong)        

       