s = "Pankaj@123!"

upper = 0
lower = 0
digits = 0
special = 0

for ch in s:
  if ch.isupper():
    upper += 1

  elif ch.islower():
    lower += 1

  elif ch.isdigit():
    digits += 1

  else:
    special += 1


print("UpperCase: ", upper)
print("LowerCase: ", lower)
print("Digits: ", digits)
print("Special: ", special)


