

#print all numbers from start to end

#read=start,end

start=int(input("enter starting number:"))

end=int(input("enter end limit:"))

if start<end:

    for num in range(start,end+1,1):
    #     if num%2==0:
    #          print(num)
        print(num)



       
else:

    for num in range(start,end-1,-1):
        # if num%2==0:
            # print(num)

        print(num)        