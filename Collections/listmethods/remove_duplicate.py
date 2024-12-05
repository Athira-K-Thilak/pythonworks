

#Removing duplicates from a list

list=[1,2,2,3,5,4,3,4,6]

list.sort()

list_without_duplicate_elements=[]

for i in range(0,len(list)-1):

    if list[i] not in list_without_duplicate_elements:

        list_without_duplicate_elements.append(list[i])

print(list_without_duplicate_elements)        