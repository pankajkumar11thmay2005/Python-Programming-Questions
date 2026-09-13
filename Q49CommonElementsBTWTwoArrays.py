a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

b_set = set(b)
common = []

for x in a:
    if x in b_set and x not in common:
        common.append(x)

print(common)