

#duplicate numbers

arr=[1,2,1,2,3,4,3,2,3]
arr.sort()
# count=0
duplicate_num=[]
for i in range(0,len(arr)-1):
    # count+=1
    j=i+1
    result=arr[j]-arr[i]
    if result==0:
        if arr[i] not in duplicate_num:
            duplicate_num.append(arr[i])
print(duplicate_num)
# print(count)       
        
               