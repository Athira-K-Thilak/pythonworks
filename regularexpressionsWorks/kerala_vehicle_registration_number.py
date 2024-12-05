

from re import fullmatch

vehicle_register_number=input("enter number:")

pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,vehicle_register_number)

if matcher==None:

    print("invalid")

else:

    print('valid')    