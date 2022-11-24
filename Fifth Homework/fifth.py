src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = []
tmp = set()

for i in src:
  if i not in tmp:
    result.append(i)
  else:
    try:
      result.remove(i)
    except ValueError:
      continue
  tmp.add(i)

print(result)
