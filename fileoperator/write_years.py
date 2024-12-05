
f=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\years.txt","w")

for year in range(1800,2025,1):

    f.write(str(year)+"\n")

f.close()    