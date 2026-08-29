n = 29
is_prime = True

if n < 2:
    is_prime = False
else:
    i = 2

    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

print("Prime" if is_prime else "Not Prime")