

student_data={
    "hari":[45,40,35],
    "vipin":[34,40,45],
    "vinay":[45,40,35],
    "bijoy":[33,38,35],
    "anvin":[32,30,40]
}

#index=1 haris average mark
#index=5 anvin average mark
# index=3


# for i,element in enumerate(student_data):

#     if i+1 ==index:
#         marks=student_data.get(element)
#         avg=sum(marks)/len(marks)
#         print(element,avg)


#student and average mark dictionary

# student_avg_mark={k:(sum(v)/len(v)) for k,v in student_data.items() }
# print(student_avg_mark)


source_word="CHICKEN"

target_word="HEN"

#kangaroo_word
character_count={ch:source_word.count(ch) for ch in source_word }

is_kangaroo_word=True

for ch in target_word:
    if ch in character_count and character_count.get(ch)>0:
         character_count[ch]-=1
    else:
         is_kangaroo_word=False

print(is_kangaroo_word)         
           
            




   