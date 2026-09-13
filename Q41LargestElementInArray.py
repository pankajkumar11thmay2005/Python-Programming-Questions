# numbers = [12, 45, 7, 89, 23]

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]

largest = numbers[0]

for x in numbers[1:]:
    if x > largest:
        largest = x

print(largest)