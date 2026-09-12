binary = input("Enter a Binary Number: ")
decimal = 0

for bit in binary:
    decimal = decimal * 2 + int(bit)

print(decimal)