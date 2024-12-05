
f=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\fruits.txt","r")

fruits=[]

for line in f:

    # fruits.append(line)  # ['apple\n', 'banana\n', 'mango\n', 'orange\n', 'apple\n', 'banana']

    fruits.append(line.rstrip("\n"))  # ['apple', 'banana', 'mango', 'orange', 'apple', 'banana']


print(fruits   )    