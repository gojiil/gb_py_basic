def Generator(n):
  for i in range(1, n+1):
    if i%2 == 1:
      yield i

mygen = Generator(int(input("Введите количество элементов: ")))
for i in mygen:
  print(i)