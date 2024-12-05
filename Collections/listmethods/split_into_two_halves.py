

#split a list into two halves

lst=[1,4,6,2,8,5]

#    0 1 2 3 4 5
 #   1 2 3 4 5 6  length=6

middle_point=len(lst)//2 # 6//2=3

lst1=lst[:middle_point] #first half 
lst2=lst[middle_point:] #second half

print(lst1) #[1,4,6]
print(lst2) #[2,8,5]

    
