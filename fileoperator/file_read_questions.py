

f=open("C:\\Users\\athir\\OneDrive\\Desktop\\pythonWorks\\database\\questions.txt","r")


words=[]

for line in f:

    line=line.rstrip("\n")
    all_words=line.split(" ")

    for w in all_words:

         words.append(w)

print(words) #['this', 'is', 'a', 'python', 'program', 'to', 'print', 'hello', 'world', 'this', 'python', 'test', 'is', 'very', 'simple', 'this', 'python', 'program', 'count', 'frequency', 'of', 'each', 'word']

word_count={k:words.count(k) for k in words} 
print(word_count)    #{'this': 3, 'is': 2, 'a': 1, 'python': 3, 'program': 2, 'to': 1, 'print': 1, 'hello': 1, 'world': 1, 'test': 1, 'very': 1, 'simple': 1, 'count': 1, 'frequency': 1, 'of': 1, 'each': 1, 'word': 1}

nested_word_count=[[v,k] for k,v in word_count.items()]

print(sorted(nested_word_count,reverse=True))


#output
# [[3, 'this'], [3, 'python'], [2, 'program'], [2, 'is'], [1, 'world'], [1, 'word'], [1, 'very'],
# .. [1, 'to'], [1, 'test'], [1, 'simple'], [1, 'print'], [1, 'of'], [1, 'hello'], [1, 'frequency'], [1, 'each'], [1, 'count'], [1, 'a']]
