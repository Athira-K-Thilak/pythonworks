#fibonacci series using while loop

range=int(input("enter range:"))

# n1=0

# n2=1

# print(n1)

# i=1

# while(i<range):

#     print(n2)

#     temp=n1+n2

#     n1=n2

#     n2=temp

#     i=i+1
prev=0
present=1
print(prev)
i=1
while(i<range):
    print(present)
    next=prev+present
    prev,present=present,next
    i=i+1
    