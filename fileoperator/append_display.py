f1=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\existing_file.txt","r")
f2=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\existing_file.txt","a")

user_input=input("enter content")

f2.write(user_input+"\n")
for line in f1:
    print(line)
   
f1.close()
f2.close()    