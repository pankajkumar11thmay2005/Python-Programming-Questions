n = int(input("Enter a Number: "))

smallest = 9

while n > 0:
  digit = n % 10

  if digit < smallest:
    smallest = digit

  n //= 10

print("The smallest digit in the number is:", smallest)
