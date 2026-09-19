s = "elephant"

frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

most_frequent = None
max_count = 0

for ch, count in frequency.items():
    if count > max_count:
        max_count = count
        most_frequent = ch

print(most_frequent)