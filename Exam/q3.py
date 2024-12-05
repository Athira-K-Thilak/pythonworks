
def most_frequent_word(text:str): 
    text_sentence=text.casefold()
    punctuaction= ".?!,:;_-()[]/""''"
    text_without_punctuation=""
    for ch in text_sentence:
        if ch not in punctuaction:
            text_without_punctuation+=ch  
    words=text_without_punctuation.split(" ")
    frequent_word={w:words.count(w) for w in words}
    key_list=[k for k in frequent_word.keys()]
    value_list=[v for v in frequent_word.values()]

    maximum_value=max(value_list)

    maximum_value_index=value_list.index(maximum_value)

    most_used_word=key_list[maximum_value_index]

    return most_used_word

print(most_frequent_word(text="Hello world! Hello everyone, Welcome to the World"))    