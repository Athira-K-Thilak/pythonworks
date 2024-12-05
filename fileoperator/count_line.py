f=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\line.txt")

line=0

for l in f:

    line+=1
print(f"no of line in this file is {line}")

f.close()
