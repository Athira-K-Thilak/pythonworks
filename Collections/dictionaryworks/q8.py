

#Given a sentence , count the frequency of each word using a dictionary

text="this is a text to find the frequency this is a simple text"

text=text.split(" ")

frequency_count={}

for  w in text:

    if w in frequency_count:

        frequency_count[w]+=1

    else:

        frequency_count[w]=1

print(frequency_count)            