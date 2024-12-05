
def largest_word(text):
    words=text.split(" ")
    words_list=list(words)
    for w in words_list:
        long=max(count(w))
    return w    
text=input("enter a text :")
print(largest_word(text))