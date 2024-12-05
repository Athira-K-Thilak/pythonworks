# TWO LETTER STATE CODE, OPTIONAL SPACE OR DASH
#TWO DIGIOT CITY CODE, OPTIONAL DASH OR SPACE
# FOUR DIGIT YEAR OF ISSUE ,AN OPTIONAL SPACE OR DASH
#SEVEN DIGITS

from re import fullmatch

licence_num=input("enter driving licence number:")

pattern="[A-Z]{2}[\- ]?[0-9]{2}[\- ]?[0-9]{4}[\- ]?[0-9]{7}"

matcher=fullmatch(pattern,licence_num)

if matcher==None:

    print("invalid")

else:

    print("valid")    