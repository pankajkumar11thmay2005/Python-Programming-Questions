sentence = "Python programming is powerful"

words = sentence.split()
longest = words[0]

for word in words[1:]:
    if len(word) > len(longest):
        longest = word

print(longest)