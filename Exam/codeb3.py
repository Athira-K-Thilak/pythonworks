def non_recursive_words(text):

    text=text.casefold()

    punctuation_marks=",!{}''"".?/()[];:-_"
    
    text_without_punc_marks=""

    for ch in text:

        if ch not in punctuation_marks:

            text_without_punc_marks+=ch

    words=text_without_punc_marks.split(" ")
    
    non_recursive={w:words.count(w) for w in words }

    non_recursive_lst=[k for k,v in non_recursive.items() if v==1] 

    return non_recursive_lst

          
print(non_recursive_words("Hello World! This is a test. Hello everyone."))    