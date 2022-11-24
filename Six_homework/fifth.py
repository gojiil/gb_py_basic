# ~$python fifth.py fifth_ex/names/users.csv fifth_ex/hobbies/hobby.csv fifth_ex/final.txt

def make_dict(argv):
  a = False
  d = dict()
  program, name_f, hobbies_f, exit_f = argv
  f_1 = open(name_f,'r',encoding = 'utf-8')
  f_2 = open(hobbies_f,'r',encoding = 'utf-8')
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
    with open(exit_f, 'w', encoding='utf-8') as f:
      for key, val in d.items():
        f.write('{}:{}\n'.format(key,val))



if __name__ == "__main__":
  import sys
  exit(make_dict(sys.argv))
  
  