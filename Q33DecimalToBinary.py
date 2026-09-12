n = int(input("Enter a Number: "))
binary = ""

while n > 0:
    remainder = n % 2
    binary += str(remainder)
    n //= 2

print(binary[::-1])