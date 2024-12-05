from re import finditer

# text="abababbaab"

text="fat cat runs very fast to catch the rat"
matcher=finditer("(at)",text)

for obj in matcher:

    print(obj.groups())

    print(obj.start(),obj.group())


