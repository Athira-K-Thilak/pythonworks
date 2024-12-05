
text="ABBACB"

recursive={}

for w in text:

    if w in recursive:

        print(w)
        break

    else:

        recursive[w]=1

            