numbers = [3, 0, 1]

n = len(numbers)
missing = n

for i, x in enumerate(numbers):
    missing ^= i ^ x

print(missing)