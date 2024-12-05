
def poll(age):

    assert age>18,"invalid age"

    print("voted")

try:

    poll(14)  

except Exception as e:
    
    print(e)

# def review(rating):

#     assert rating>0,"too low"

#     assert rating<10,"too high"

#     print("rated")  

# try: 

#     review(-1)

# except Exception as e:

#     print(e)    

    
    
    


