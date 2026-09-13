numbers = [2, 2, 2, 8, 2, 9]
target = 2

frequency = 0

for x in numbers:
    if x == target:
        frequency += 1

print(frequency)