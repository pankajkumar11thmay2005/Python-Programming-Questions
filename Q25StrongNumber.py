n = 145
original = n

factorial = [1] * 10

for i in range(1, 10):
    factorial[i] = factorial[i - 1] * i

total = 0

while n > 0:
    digit = n % 10
    total += factorial[digit]
    n //= 10

print("Strong Number" if total == original else "Not Strong Number")