s = "abababa"
pattern = "aba"

count = 0
start = 0

while True:
    index = s.find(pattern, start)

    if index == -1:
        break

    count += 1
    start = index + len(pattern)

print(count)