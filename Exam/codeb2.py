def count_vowels(string):
    vowels="a,e,i,o,u"
    count=0
    for ch in  string:
        if ch in vowels:
            count+=1
    return print(count)
count_vowels("hello world")
        


            