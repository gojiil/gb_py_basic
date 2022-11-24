list = []
sum = 0

#список end[] ввожу для проверки
#end = []

for a in range(1001):
  if a%2 == 1: 
    list.append((a**3))
#    print(a**3)

for a in list:
  i = 0
  b = a
  while a > 0:
    i += a % 10
    a //= 10
  if i % 7 == 0:
#    end.append(b)
    sum = sum + b

#print(end)
print(sum)
sum = 0

#end.clear()
print("\n")

for i in range(len(list)):
  list[i] += 17

for a in list:
  i = 0
  b = a
  while a > 0:
    i += a % 10
    a //= 10
  if i % 7 == 0:
#    end.append(b)
    sum = sum + b

#print(end)
print(sum)
