
text="ABAABBBC"

#most recursive character

#least recursuve character



def get_count(ch):

    return text.count(ch)

most_recursive_character=max(text,key=get_count)

print(most_recursive_character)

least_recursive_character=min(text,key=get_count)

print(least_recursive_character)