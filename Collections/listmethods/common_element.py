
#common element in two list

list1=[1,2,3]
list2=[1,2,3,4,6]
list1.sort()
list2.sort()
i=0
j=0
while(i<=len(list1)-1 and j<=len(list2)-1):
    if list1[i]==list2[j]:
        print(list1[i])
        i+=1
        j+=1
    elif list1[i]<list2[j]:
        i+=1
    elif list1[i]>list2[j] :
        j+=1
        
