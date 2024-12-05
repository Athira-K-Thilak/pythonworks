

# email="athira@gmail.com"

# index=email.index("@")

# print(email[:index])

# text="vipinkumar@gmail.com"

# print(text[0:text.index("@")])


text="hellopython"

o_index=text.index("o")

reversed_sub_str=text[o_index-1::-1]

print(reversed_sub_str)

balance_sub_str=text[o_index:]

result=reversed_sub_str+balance_sub_str

print(result)
