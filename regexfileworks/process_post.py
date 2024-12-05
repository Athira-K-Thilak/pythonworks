from re import finditer

f=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\regexfileworks\\social_post.txt")

for line in f:

    words=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,words)

    for obj in matcher:

        print(obj.group())

