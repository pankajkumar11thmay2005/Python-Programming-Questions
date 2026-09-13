numbers = [2, 7, 4, 9, 10, 13]

even = 0
odd = 0

for x in numbers:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)