

def is_palindrome_number(number):

    original_num=number

    reverse=0

    while(number>0):

        digit=number%10

        reverse=reverse*10+digit

        number=number//10

    print("Palindrome" if reverse==original_num else "not palindrome")

is_palindrome_number(15351)        