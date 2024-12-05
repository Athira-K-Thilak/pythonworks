
arr=[100,200,300,400,500,600,700,800]

# odd_positioned_elements=[arr[i] for i in range(0,len(arr)) if i%2!=0]

# print(odd_positioned_elements)

# odd_positioned_elements.reverse()

odd_positioned_elements=[num for index,num in enumerate(arr)  if index%2!=0]

odd_positioned_elements.reverse()
print(odd_positioned_elements)
i=1

for index,num in enumerate(odd_positioned_elements):

    arr[i]=num

    i+=2
print(arr)








