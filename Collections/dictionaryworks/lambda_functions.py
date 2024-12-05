#  lambda functions

# lambda function for adding two numbers
add=lambda num1,num2:num1+num2
print(add(100,200))

#lambda function for finding cube of a number
cube=lambda num:num**3
print(cube(3))

#lambda function for subtracting two numbers
sub=lambda n1,n2:n1-n2
print(sub(10,2))

#large string
max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2
print(max_two("apple","mangoes"))

#mininum length string(small string)
min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2
print(min_two("apple","mangoes"))

#smart subtraction
smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1
print(smart_sub(20,100))


# largest word in the list
words=["hello","hai","morning","test","apple"]

# def get_length(str1):

#     return len(str1)

# print(max(words,key=get_length))
# print(min(words,key=get_length))

#by using lambda function largest word in the list


get_length=lambda str:len(str)
print(max(words,key=get_length))

#functions for sorting and etc
 # sorted()
# min()
# max()
# sum()

