

# merge two list and sort resulting list

list1=[1,2,4,6,7,9]

list2=[8,5,3,10]

result=[]

for i in list1:

    result.append(i)

for j in list2:

        result.append(j)    

print("Resulting list is",result)    

result.sort()

print(" sorted resulting list is ",result)
