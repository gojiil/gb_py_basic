import random

k = int(input("Введите длину первичного списка: "))
src = [random.randint(1,501) for num in range(k)]
print(src)

#src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 250]

result = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
print (result)