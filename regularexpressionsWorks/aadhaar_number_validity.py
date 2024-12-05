#TOTAL 12 DIGITS: should not start with 0 or 1 or special characterss
#after 4 numbers there should be white space between another 4 numbers
#should not contain any alphabets or special characters and should have only numbers

from re import fullmatch

aadhaar_num=input("enter aadhar number:")

pattern="[2-9][0-9]{3}[ ][0-9]{4}[ ][0-9]{4}"

matcher=fullmatch(pattern,aadhaar_num)

if matcher==None:

    print("invalid")

else:

    print("valid")    
