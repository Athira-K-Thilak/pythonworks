
#find least positive missing integer 
#sample 1
# arr1=[1,3,4,5]

#sample 2
# arr1=[2,3,5]

# i=1

# while(i<=len(arr1)-1):

#     if arr1[i] not in arr1:

#         print(arr1[i])

#     i+=1    

arr=[1,2,5,4] 

arr.sort()

# diff=0
for i in range(0,len(arr)-1):
    
    j=i+1
    # diff=arr[j]-arr[i]
    result=arr[j]-arr[i]

    if result!=1:

      print(arr[i]+1," is missing number")
      
      break
      
