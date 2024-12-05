f=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\word_text.txt")
text=""

for line in f:
    text+=line

word=text.strip(" ")

count=0

for w in word:

    count+=1

print(f"no of words in this text is {count}")

f.close()
