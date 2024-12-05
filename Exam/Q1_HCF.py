
num1=int(input("enter number 1:"))

num2=int(input("enter number 2:"))

hcf=1

min_num=min(num1,num2)

for i in range(1,min_num+1):

    if num1%i==0 and num2%i==0:

        hcf=i

print(hcf)        