from re import finditer

text="I have 3 cars,2 bike and 1-cycle"

# pattern="\w" # "[a-zA-Z0-9]" alphanumeric
# pattern='\d' #"[0-9]" digiit
# pattern="\D" #"[^0-9]" exclude digits
# pattern="\W" #SPECIAL CHARACTERS "[^a-zA-Z0-9]"
# pattern="\s" #space
pattern="\S" #exclude space 

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())