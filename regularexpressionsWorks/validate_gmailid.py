from re import fullmatch

gmailid=input("enter gmailid:")

pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"

matcher=fullmatch(pattern,gmailid)

print("invalid" if matcher==None else "valid")