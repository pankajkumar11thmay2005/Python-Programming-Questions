s = "programming"

seen = set()
result = []

for ch in s:
    if ch not in seen:
        result.append(ch)
        seen.add(ch)

print("".join(result))