

arr=[2,3,4,5]

sum=int(input("enter value:"))

# for i in range(0,len(arr)-1):

#     for j in range(i+1,len(arr)):

#         curr_sum= (arr[i]+arr[j])

#         if curr_sum==sum:

#             print((arr[i],arr[j]))

#             break

left=0

right=len(arr)-1

while(left<right):

    cur_sum=arr[left]+arr[right]

    if cur_sum==sum:

        print((arr[left],arr[right]))

        right-=1

        left+=1
        # break
    elif cur_sum>sum:

        right-=1

    elif cur_sum<sum:

        left+=1    

        