n = 153
original = n
digits = len(str(n))
total = 0

while n > 0:
    digit = n % 10
    total += digit ** digits
    n //= 10

print("Armstrong" if total == original else "Not Armstrong")