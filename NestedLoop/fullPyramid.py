

size=int(input("enter size:"))

for row in range(1,size):

    for sp in range(1,size-row):

        print(" ",end="")

    for col in range(1,row+1):

        print("* ",end="")    

    print()        

     