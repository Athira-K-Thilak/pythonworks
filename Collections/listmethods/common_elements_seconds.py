
arr1=[10,12,11,14,15,16]

arr2=[20,10,15,13,16]

arr1.sort()

arr2.sort()

p1=0

p2=0

counter=0

while(p1<len(arr1) and p2<len(arr2)):
    counter+=1

    if arr1[p1]==arr2[p2]:

        print(arr1[p1])

        p1+=1

        p2+=1

    elif arr1[p1]<arr2[p2]:

        p1+=1

    elif arr1[p1]>arr2[p2]:

        p2+=1        
print("count=",counter)
        