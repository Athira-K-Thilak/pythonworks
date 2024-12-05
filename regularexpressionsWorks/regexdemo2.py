from re import finditer

text="I have 3 cars,2 bike and 1-cycle" 

# pattern="[a-z]" #chk all lowercase alphabet

# pattern="[a-zA-Z]"#chk for all alphabets

# pattern="[0-9]" #chk for digits

#alphanumeric
# pattern="[a-zA-Z0-9]"#chk for all alphanumeric

# pattern="[^ak]"#exclude a,k

#all lowercase alphabets exclude a,k
# pattern="[^akA-Z0-9,\- ]"

# pattern="[^a-zA-Z0-9]" #chk for special characters
pattern="[\W]"#EXCLUDE ALPHANUMERIC 
matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),"==>",obj.group())