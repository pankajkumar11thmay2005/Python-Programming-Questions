s = '1234456'

is_digit = True

for ch in s:
  if ch < '0' or ch > '9':
    is_digit = False
    break

print(is_digit)