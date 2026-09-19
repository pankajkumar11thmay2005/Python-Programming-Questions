p = "Pankaj is a very good boy."

result = ""

for ch in p:
  if ch == ' ':
    result += '-'
  else:
    result += ch

print(result)