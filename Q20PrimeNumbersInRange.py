start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for n in range(start, end + 1):
    if n < 2:
        continue

    is_prime = True
    i = 2

    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(n, end=" ")