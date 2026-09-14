s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print("Not Anagrams")
else:
    freq1 = {}
    freq2 = {}

    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1

    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1

    print("Anagrams" if freq1 == freq2 else "Not Anagrams")