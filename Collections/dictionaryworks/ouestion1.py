
arr=[10,20,30,40,2,3]

# result={}

# for num in arr:

#     if num not in  result:

#         result[num]=num**2

# print(result) 
# 
# logic 2       
      
# for num in arr:

#     square=num**2

#     result[num]=square

# print(result)

#dictionary comprehension

# result={num:num**2 for num in arr }

# print(result)

#even numbers squares

even_squares={num:num**2 for num in arr if num%2==0}

odd_cubes={num:num**3 for num in arr if num%2!=0}

print(even_squares)

print(odd_cubes)

arr1=[10,20,30,40,2,3,7,8,9,10,30]

frequency_count={num:arr1.count(num) for num in arr1}

print(frequency_count)