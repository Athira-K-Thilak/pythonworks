
num1=int(input("enter num1:"))

num2=int(input('enter num2:'))

num3=int(input("enter num3:"))

if num1>num2 and num1>num3:
    
    if num2>num3:

        print("num2 is second largest")

    else:
        print("num3 is second largest") 

elif num2>num3 and num2>num3:

    if num1>num3:

        print("num1 is second largest")

    else:

        print("num3 is second largest")

elif num3>num1 and num3>num2:

    if num2>num3:

        print("num2 is second largest")

    else:

        print('num3 is second largest')                          