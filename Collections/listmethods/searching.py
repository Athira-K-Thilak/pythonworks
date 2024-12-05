

#binary search

arr=[10,8,7,12,13,20,25]

#read search element from user

serach_element=int(input("enter a number:"))

is_present=False

#sort away

arr.sort()

#set pointers

low=0

upp=len(arr)-1

while(low<=upp):

    mid=(low+upp)//2

    #case1

    if serach_element==arr[mid]:

        is_present=True

        break

    elif serach_element<arr[mid]:

        upp=mid-1

    elif serach_element>arr[mid]:

        low=mid+1

print(is_present)            

    

