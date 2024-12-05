

#list comprehension

# arr=[2,3,4,5,6,7]

#output square_list

# square_list=[]

# for i in  arr:

#     i**=2

#     square_list.append(i)

# print(square_list)    
#cubes

# cubes=[]
# for num in arr:
#     cubes.append(num**3)
# print(cubes) 
# 
# comprehension minimalize the steps to one line
# 
#syntax
# [return loop condition]   ifyou want to assign it to a variable you can use it 
# 
# cubes
# cube=[num**3 for num in arr]  
# print(cube)

# squares=[num**2 for num in arr]
# print(squares)

# add_fives=[num+5 for num in arr]
# print(add_fives)

# arr=[2,3,4,5,6]

# add_ten=[num+10 for num in arr]
# print(add_ten)
# even_numbers=[num for num in arr if num%2==0]
# print(even_numbers)
# odd_numbers=[num for num in arr if num%2!=0]
# print(odd_numbers)
# numbers_gt_five=[num for num in arr if num>5]
# print(numbers_gt_five)

# arr=[2,3,4,5,6,7]
# map_num=[num+1 if num>5 else num-1 for num in arr]
# print(map_num)

# text=["apple","iphone","orange","potato"]

# #words starting with vowel

# start_with_vowel=[txt for txt in text if txt[0]=="a" or txt[0]=="e" or txt[0]=="i" or txt[0]=="o" or txt[0]=="u"]

# print(start_with_vowel)



# text=["apple","iphone","orange","potato"]

# #all words to upper case

# text_upper_case=[txt.upper() for txt in text]

# print(text_upper_case)

# text=["apple","iphone","orange","potato"]

# consonant_words=[w   for  w in text if w[0] not in ['a','e','i','o','u']]

# print(consonant_words)


#longest word

# text=["apple","iphone","orange","potatto",'tomatto',"kiwi"]

# long=max([len(w) for w in text])
# print(long)

# longest_word=[w for w in text if len(w)==long]

# print(longest_word)

# short=min([len(w) for w in text])

# shortest_word=[w for w in text if len(w)==short]
# print(shortest_word)

      

