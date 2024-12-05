

#print first 5 fibonacci numbers 

# n1=0

# n2=1

# print(n1) 

# for i in range(1,5):

#     print(n2)

#     temp=n1+n2 

#     n1=n2  

#     n2=temp 

prev=0
current=1
print(prev)
for i in range(1,5):
    print(current)
    next=prev+current
    prev,current=current,next
    