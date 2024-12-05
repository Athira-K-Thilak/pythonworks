
number=int(input("enter a number:"))

prev=0

current=1

is_fibo=False

for i in range(1,number+1):

    next=prev+current

    prev=current

    current=next

    if next==number:

        is_fibo=True

        break

print(is_fibo)

        