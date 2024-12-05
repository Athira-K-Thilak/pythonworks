
arr1=[10,13,8,11,20]

arr2=[2,20,8,7,13]

#common elements without using "in" 13,20,8

# for i in arr1:
#     for j in arr2:
#         if i==j:
#             print(i)
counter=0
for i in range(1,len(arr1)):
    for j in range(1,len(arr2)):

        counter+=1
        if arr1[i]==arr2[j]:
            print(arr1[i])

print("count=",counter)            