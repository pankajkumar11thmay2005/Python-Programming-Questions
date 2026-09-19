s = 'Pankaj'
result = ""

for ch in s:
  if ch.isupper():
    result += ch.lower()

  else:
    result += ch.upper()


print(result)