# numbers = [10, 25, 8, 42, 17]

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]

largest = float("-inf")
second_largest = float("-inf")

for x in numbers:
    if x > largest:
        second_largest = largest
        largest = x
    elif x > second_largest:
        second_largest = x

print(second_largest)