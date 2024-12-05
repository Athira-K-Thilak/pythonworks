

text='this is a simple programming question to find word with maximum number of characters'
#split the text into words
words=text.split(" ")

# def get_length(w):

#     return len(w)

# srt_words=sorted(words,key=get_length,reverse=True)

# print(srt_words)


#most recursive word

def get_count(w):

    return words.count(w)

frequency_word=max(words,key=get_count)

print(frequency_word,words.count(frequency_word))