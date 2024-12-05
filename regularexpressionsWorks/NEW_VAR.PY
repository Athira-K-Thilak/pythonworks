
#STARTING WITH AN ALPHABET FROM p-t

#in second place must be a number divisible by 3

# followed by any number alphabets,numbers,@
#s6abc  valid
#a6vvhvh invalid
#s7bc   invalid


from re import fullmatch

pattern="[p-tP-T][369][a-zA-Z0-9@]*"

user_input=input("enter variable name:")

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("Invalid")

else:

    print("valid")    