

text='ABBECBAC'


# def get_count(ch):
#     return text.count(ch)
get_count=lambda ch:text.count(ch)

most_recursive=max(text,key=get_count)
print(most_recursive)