from re import findall

f=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\regexfileworks\\urls.txt")

content=f.read()

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)