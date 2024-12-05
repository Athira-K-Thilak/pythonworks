from re import fullmatch,findall

f=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\regexfileworks\\data.txt")

content=f.read()

pattern="[[0-9]{2}/[0-9]{2}/[0-9]{4}"

all_dates=findall(pattern,content)

for date in all_dates:

    print(date)