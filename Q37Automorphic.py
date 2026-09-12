n = int(input("Enter a number: "))

digits = len(str(n))
square = n * n
last_digits = square % (10 ** digits)

if last_digits == n:
    print("Automorphic")
else:
    print("Not Automorphic")