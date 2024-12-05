

# lst=[]
# tp=()

# st=set() #if you define it with{} it will not create an empty set instead it will create dictionary

# st={10,20,30}

# print(st)

# s={10,20,10,30,40,20,50} #will not allow duplicates

# print(s)

colors={"red","green",'blue'}

colors.add("yellow")

# print(colors)

# st1={1,2,3}

# st2={1,2,3,4,5}

# #subset- 

# print(st1.issubset(st2))# True or False

# #superset- if all the elements of one set belongs to another set its superset

# print(st2.issuperset(st1))

# st1={1,2,3,10,20}

# st2={1,2,3,4,5}

# syymetric_difference=st1.symmetric_difference(st2)
# print(syymetric_difference)

#update()

st1={1,2,3,10,20}
st2={1,2,3,4,5}
st1.update(st2)
# print(st1)

text="this is a test to remove duplicate words this test is simple"

# sp_test=text.split(" ")
# print(set(sp_test))
text2="this simple test remove duplicate words"
is_correct=False
words_text=text.split(" ")
words_text2=text2.split(" ")
print(set(words_text).difference(words_text2))