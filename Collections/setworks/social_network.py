

users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_followers=["sanju","rohit","kohli"] #mutal friends

mutual_friends=set(rahul_followers).intersection(set(sanju_followers))

print(mutual_friends)

#followers_suggestions ["sanju","pandya","siraj"]

# users_set=set(users)

# rahul_followers_set=set(rahul_followers)

# followers_suggestion=users_set.difference(rahul_followers)

# print(followers_suggestion)

# print(list(followers_suggestion))
rahul_follow_suggestion=set(users).difference(set(rahul_followers))

print(rahul_follow_suggestion)