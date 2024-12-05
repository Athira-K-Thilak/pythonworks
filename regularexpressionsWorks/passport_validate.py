#total of 8 characters  
#first character should be uppercae alphabet
#next two characters - first number from 1-9 and 2nd number from 0-9
#fourth zero or white space
#next four any from 0-9
#last character should be any number from 1-9

from re import fullmatch

passport_number=input("enter passport number:")

pattern="[A-Z][1-9][0-9][0 ]?[0-9]{3}[1-9]"

matcher=fullmatch(pattern,passport_number)

if matcher==None:

    print('invalid')

else:

    print("valid")    