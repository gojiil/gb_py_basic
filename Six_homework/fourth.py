# Реализовал Словарь таким образом, что ключи - это кортежи (tuple), а значения - списки (list).
# Обосновано это тем, что ФИО у человека всегда одно и то же, а увлечения могут меняться.

import os.path

users = "Иванов,Иван,Иванович\nПетров,Петр,Петрович\nПавлов,Игорь,Геннадьевич"
hobbies = "скалолазание,охота\nгорные лыжи"

d = {}
a = False

check_files = os.path.exists("third_ex/users.csv") & os.path.exists("third_ex/hobby.csv")
print("Наличие файлов:",check_files)

if check_files == False:
  with open('third_ex/users.csv', 'w', encoding='utf-8') as f:
    f.write(users)
  
  with open('third_ex/hobby.csv', 'w', encoding='utf-8') as f:
    f.write(hobbies)
  
  print("Updating done!")

f_1 = open('third_ex/users.csv','r',encoding = 'utf-8')
f_2 = open('third_ex/hobby.csv','r',encoding = 'utf-8')
l_1 = f_1.readline().replace("\n","")
l_2 = f_2.readline().replace("\n","")

while l_1:
  while l_2:
    try:
      line_1 = l_1.split(",")
      line_2 = l_2.split(",")
      tup_1 = (line_1[0],line_1[1],line_1[2])
      d[tup_1] = line_2
      l_1 = f_1.readline().replace("\n","")
      l_2 = f_2.readline().replace("\n","")
    except IndexError:
      a = True
      print("Error: 1")
      break
  
  if l_1 != '':
    line_1 = l_1.split(",")
    tup_1 = (line_1[0],line_1[1],line_1[2])
    d[tup_1] = None
    l_1 = f_1.readline().replace("\n","")
    
  
f_1.close()
f_2.close()

if a == False:
  print(d)