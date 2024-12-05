#searching
#linear
#binary

arr=[2,4,6,3,8,7]

search_element=int(input("enter number"))

is_present=False

for i in range(0,len(arr)-1):

    if search_element==arr[i]:

        is_present=True

        break

print(is_present)