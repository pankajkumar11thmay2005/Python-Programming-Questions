n = int(input("Enter a Number: "))

while n > 1 and n % 2 == 0:
    n //= 2

if n == 1:
    print("Power of 2")
else:
    print("Not a Power of 2")