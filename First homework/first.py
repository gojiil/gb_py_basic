# Введено для проверки на ноль
day = 0
hour = 0
min = 0
sec = 0

# Список переменных
time_in_sec = list(map(int,input("Введите промежутки в сек. через пробел: ").split()))
print("\n")

# Основное тело цикла
for i in range(len(time_in_sec)):
  while time_in_sec[i] > 0:
      sec = time_in_sec[i] % 60
      time_in_sec[i] = time_in_sec[i] // 60
      min = time_in_sec[i] % 60
      time_in_sec[i] = time_in_sec[i] // 60
      hour = time_in_sec[i] % 24
      day = time_in_sec[i] // 24
      time_in_sec[i] = 0

  print("Промежуток №",(i+1))
  if day > 0:
      print(f"{day} days, {hour} hours, {min} minutes, {sec} seconds")
  elif hour > 0:
      print(f"{hour} hours, {min} minutes, {sec} seconds")
  elif min > 0:
      print(f"{min} minutes, {sec} seconds")
  else:
      print(f"{sec} seconds")
  print("\n")
