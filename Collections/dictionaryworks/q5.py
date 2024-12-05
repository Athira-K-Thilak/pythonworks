"""write a python  program  to create  a dictionary from a list 
   of keys and values using dictionary comprehension"""

lst=["hai","hello","hai","hello","hai"]

count_lst={i:lst.count(i) for i in lst}

print(count_lst)