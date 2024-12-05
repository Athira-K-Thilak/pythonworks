

def sort_numbers(*args,**kwargs):

    if kwargs.get("reverse")==True:


        return sorted(args,reverse=True) #descending order
    
    if kwargs.get("reverse")==False:

        return sorted(args,reverse=False)#ascending order
    

print(sort_numbers(10,45,20,3,55,reverse=True))  

print(sort_numbers(10,45,20,3,55,reverse=False))    