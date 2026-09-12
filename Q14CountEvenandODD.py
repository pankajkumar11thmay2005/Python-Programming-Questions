a = int(input("Enter The Number: "))

even = 0
odd = 0

while a > 0:
  digit = a % 10

  if digit % 2 == 0:
    even += 1

  else:
    odd += 1

  a = a // 10

print("Even digits:", even)
print("Odd digits:", odd)