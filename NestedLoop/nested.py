

#logic


#  #

#  #

# end=int(input("enter an ending point:"))

# for row  in range(1,end+1):

#     for col in range(1,end+1):

#         print("#",end="\t")

#     print()    


#logic of half pyrmid(inverted)
# for row in range(5,0,-1):

#     for col in range(1,row+1):

#         print("@",end="\t")

#     print()    

#logic of full pyramid

# for row in range(1,5):

#     for sp in range(1,5-row):

#         print(" ",end="")

#     for col in range(1,row+1):

#         print("* ",end="")
        
#     print()        

    #logic of full pyramid inverted

size=int(input("enter size:"))

for row in range(size-1,0,-1):

        for sp in range(1,size-row):

          print(" ",end="")

        for col in range(1,row+1):

            print("* ",end="")
        
        print()        