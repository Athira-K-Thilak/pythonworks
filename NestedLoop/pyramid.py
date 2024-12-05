
#square
# n=3
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()   

# Rectangle
# r=3
# c=6
# for i in range(r):
#     for j in range(c):
#         print("*",end=" ")
#     print()     

#increasing triangle
# n=3
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()    

#decreasing triangle
# n=3
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()    

#right sided triangle                       *
# n=3                            #        * *
# for i in range(n):             #      * * *    
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()        

#decreasing right sided triangle
# n=3                       #          * * *
# for i in range(n):        #            * *
#     for j in range(i+1):  #              *
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

#pyramid(inverted)
n=3
for i in range(n):
    for sp in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end=" ")  
    print()

#pyramid
# n=5
# for i in range(n):
#     for sp in range(n-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")  
#     print()

#diamond    
# n=int(input("enter size ="))
# for i in range(n+1):
#     for sp in range(n-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")  
#     print()  
# for i in range(n):
#     for sp in range(i+1):
#         print(" ",end="")
#     for j in range(n-i):
#         print("*",end=" ")  
#     print()

#  
# n=int(input("enter size ="))  
# for i in range(n):
#     for sp in range(i+1):
#         print(" ",end="")
#     for j in range(n-i):
#         print("*",end=" ")  
#     print()
# for i in range(n):
#     for sp in range(n-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")  
#     print() 