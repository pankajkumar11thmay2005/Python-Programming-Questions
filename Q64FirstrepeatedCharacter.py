p = "acbadqbwmb"

seen = set()

for ch in p:
  if ch in seen:
    print(ch)
    break

  seen.add(ch)


