
"""given two lists,one with fruits and the other with prices,
write a dictionary comprehension to pair them together into a dictionary"""

fruits=["Pear","Apple","orange","Avacado"]

price=[210,200,150,300]

# zip() function used to combine two or more iterable dictionaries into single iterable 

fruit_price={k:v for k,v in zip(fruits,price)} 

print(fruit_price)    

