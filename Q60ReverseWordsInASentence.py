sentence = "Python is very powerful"

words = sentence.split()
result = []

for i in range(len(words) - 1, -1, -1):
    result.append(words[i])

print(" ".join(result))