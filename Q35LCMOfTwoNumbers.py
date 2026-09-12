a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

x, y = a, b

while y != 0:
    x, y = y, x % y

gcd = x
lcm = (a * b) // gcd

print(lcm)