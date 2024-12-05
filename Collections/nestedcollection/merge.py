lst1=["apple","mango","onion","potato"]

lst2=[100,200]

result={}

for i in range(0,len(lst2)):

    lst1_index_element=lst1[i]
    lst2_index_element=lst2[i]
    result[lst1_index_element]=lst2_index_element

print(result)    

balance_elements=lst1[len(lst2):]

print(balance_elements)

for index,element in enumerate(balance_elements):

    result[element]=index+1

print(result)    

#{'apple': 100, 'mango': 200, 'onion': 1, 'potato': 2}