string = "в 5 часов 17 минут температура воздуха была +5 градусов"
list = string.split()
print("Изначальный список: \n",list)

new_list = []
string = ""

for i in range(len(list)) :
  
  try:
    
    if int(list[i]) and list[i].find("+") == (-1) : 
      list[i] = list[i].zfill(2)
      new_list.append('"')
      new_list.append(list[i])
      new_list.append('"')
      string += str(new_list[-3:-2]).strip("['']") + str(new_list[-2:-1]).strip("['']") + str(new_list[-1:]).strip("['']") + " "
      
    elif int(i) // 10 == 0 :
      list[i] = list[i].zfill(3)
      new_list.append('"')
      new_list.append(list[i])
      new_list.append('"')
      string += str(new_list[-3:-2]).strip("['']") + str(new_list[-2:-1]).strip("['']") + str(new_list[-1:]).strip("['']") + " "
  
  except ValueError:
    new_list.append(list[i])
    string += str(new_list[-1:]).strip("['']") + " "

print("Измененный список: \n", list)
print("Список с кавычками: \n", new_list)
print("Строчное представление: \n", string)