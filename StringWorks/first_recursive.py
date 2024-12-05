text="ABCABC"

recursive=""

for ch in text:

    if ch not in recursive:

        recursive+=ch

    else:

        print(ch)

        # print(f"first recursive character is {ch} ")

        break    