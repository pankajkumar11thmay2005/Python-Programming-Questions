s = "The quick brown fox jumps over the lazy dog"

letters = set()

for ch in s.lower():
    if 'a' <= ch <= 'z':
        letters.add(ch)

if len(letters) == 26:
    print("Pangram")
else:
    print("Not Pangram")