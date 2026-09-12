base = int(input("Enter a Base Number: "))
exponent = int(input("Enter an Exponent: "))
result = 1

for _ in range(exponent):
    result *= base

print(result)