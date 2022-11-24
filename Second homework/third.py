string = "в 5 часов 17 минут температура воздуха была +5 градусов"
list = string.split()
print("Изначальный список: \n",list)

# TODO: Доделать реализацию списка с кавычками (кавычки до и после каждого числа)

string = ""

for i in list :
  
  try:
    
    if int(i) and i.find("+") == (-1) : 
      i = str(i)
      old = i
      k = list.index(i)
      list[k] = i.zfill(2)
    
    elif int(i) // 10 == 0 :
      i = str(i)
      k = list.index(i)
      list[k] = i.zfill(3)
  
  except ValueError:
    continue

print("Измененный список: \n",list)


j = 0
for i in list :
  
  try:
    
    if int(i) and int(i) != j: 
      j = int(i)
      k = list.index(i)
      list.insert(k+1,'"')
      list.insert(list.index(i),'"')
      string += list[k] + list[k+1] + list[k+2] + " "
    
    else: 
      continue
  
  except ValueError:
    if i != '"':
      k = list.index(i)
      string += list[k] + " "
    continue

print("Список с кавычками: \n",list)
print("Строчное представление: \n", string)