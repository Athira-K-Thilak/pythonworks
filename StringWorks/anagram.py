
source_word="silent"

target_word="listen"

is_anagram=True

for ch in source_word:

    if ch not in  target_word:

        is_anagram=False

        break

print(is_anagram)
