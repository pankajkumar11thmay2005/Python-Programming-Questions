n = int(input("Enter a Number: "))

target = 4
count = 0

while n > 0:
  digit = n % 10

  if digit == target:
    count += 1

  n //= 10

print(count)