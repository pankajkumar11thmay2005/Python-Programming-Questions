n = int(input("Enter a number: "))

largest_digit = 0

while n > 0:
    digit = n % 10

    if digit > largest_digit:
        largest_digit = digit
    n //= 10

print("The largest digit in the number is:", largest_digit)