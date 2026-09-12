n = int(input("Enter a number: "))
divisor_sum = 0

for i in range(1, n):
    if n % i == 0:
        divisor_sum += i

if divisor_sum == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")