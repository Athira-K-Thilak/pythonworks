
f_read=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\words.txt")

f_write=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\palindromes.txt","w")

for line in f_read:

    word=line.rstrip("\n")

    reversed_word=word[::-1]

    if word==reversed_word:

        f_write.write(word+"\n")

f_read.close()

f_read.close()

