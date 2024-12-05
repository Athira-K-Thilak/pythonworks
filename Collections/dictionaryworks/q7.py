

"""write a python program to filter a dictionary,keeping only items with values greater
  than 50 using dictionary comprehension"""

products={"milk":28,"apple":200,"Biscuit":25,"avacado":300}

value_above_50={k:v for k,v in products.items() if v>50}

print(value_above_50)