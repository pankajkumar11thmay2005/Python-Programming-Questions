# numbers = input("Enter numbers separated by spaces: ").split()
# numbers = [float(num) for num in numbers]

n = {12, 15, 20, 25, 30}

total = 0

for num in n:
    total += num

average = total / len(n)

print(average)