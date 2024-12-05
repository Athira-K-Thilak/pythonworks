# """given a dictionary of items and their prices ,write a program to
#    apply a 10% discount to all the items using dictionary comprehension


items={"apple":200,"orange":150,"pear":200,"avacado":320}

discount_price={k:v-((10*v)/100) for k,v in items.items()}

print(discount_price) #  dictionary contains items with price of product after applying the discount