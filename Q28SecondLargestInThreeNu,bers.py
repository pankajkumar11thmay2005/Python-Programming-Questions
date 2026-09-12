a, b, c = int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: "))

largest = float("-inf")
second = float("-inf")

for x in (a, b, c):
    if x > largest:
        second = largest
        largest = x
    elif x > second:
        second = x

print(second)