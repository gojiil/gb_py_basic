import os.path

users = "Иванов,Иван,Иванович\nПетров,Петр,Петрович\nПавлов,Игорь,Геннадьевич"
hobbies = "скалолазание,охота\nгорные лыжи"

d = {}
a = False

check_file = os.path.exists("third_ex/users.csv") & os.path.exists("third_ex/hobby.csv")
print(check_file)

if check_file == False:
  with open('third_ex/users.csv', 'w', encoding='utf-8') as f:
    f.write(users)
  
  with open('third_ex/hobby.csv', 'w', encoding='utf-8') as f:
    f.write(hobbies)
  
  print("Updating done!")

f_1 = open('third_ex/users.csv','r',encoding = 'utf-8')
f_2 = open('third_ex/hobby.csv','r',encoding = 'utf-8')
line_1 = f_1.readline()
line_2 = f_2.readline()
while line_1:
  while line_2:
    try: 
      d[line_1.replace("\n","")] = line_2.replace("\n","")
      line_1 = f_1.readline()
      line_2 = f_2.readline()
    except IndexError:
      a = True
      print("Error: 1")
      break
  
  if line_1 != '':
    d[line_1.replace("\n","")] = None
    line_1 = f_1.readline()
  
f_1.close()
f_2.close()

if a == False:
  print(d)