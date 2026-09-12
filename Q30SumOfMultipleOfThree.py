start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
total = 0

for i in range(start, end + 1):
    if i % 3 == 0:
        total += i

print(total)