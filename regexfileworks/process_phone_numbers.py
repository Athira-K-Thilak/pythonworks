from re import fullmatch

f=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\regexfileworks\\phone_numbers.txt")

for line in f:

    phone=line.strip("\n")

    pattern="(91)?[0-9]{10}"

    matcher=fullmatch(pattern,phone)

    if matcher !=None:

        print(phone)