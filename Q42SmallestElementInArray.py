# numbers = [12, 45, 7, 89, 23]

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]

smallest = numbers[0]

for x in numbers[1:]:
    if x < smallest:
        smallest = x

print(smallest)