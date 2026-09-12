# numbers = [10, -2, 0, 5, -7, 0]

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]

positive = 0
negative = 0
zero = 0

for x in numbers:
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)