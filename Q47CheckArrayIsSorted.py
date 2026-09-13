numbers = [1, 2, 2, 4, 7]

is_sorted = True

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break

print("Sorted" if is_sorted else "Not Sorted")