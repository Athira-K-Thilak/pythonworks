# text="this is a simple program count the word count this program is simple"

words=["hai","hello",'yoo','hello',"hai","hai"]



words_count={}

for w in words:

    if w in words_count:

        words_count[w]+=1

    else:

        words_count[w]=1

print(words_count)           