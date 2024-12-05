
f_write=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\q1write.txt","w")

f_read=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\q1write.txt")

user_input=input("enter content")

f_write.write(user_input+"\n")
print(user_input)




f_write.close()

f_read.close()