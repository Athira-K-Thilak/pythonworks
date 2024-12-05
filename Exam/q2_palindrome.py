

def is_palindrome(string:str):

    original_string=string

    reversed_string=original_string[::-1]

    if original_string==reversed_string:

        is_correct=True

    else:

        is_correct=False 

    return is_correct
    
    
print(is_palindrome("racecar"))




