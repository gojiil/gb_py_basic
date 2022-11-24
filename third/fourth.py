def thesaurus(list):

  seq = []
  d = dict()
  
  for i in list:
    seq += i[0]

  seq = set(seq)
  
  for i in seq:
    for k in list:
      if k[0] == i:
        d.setdefault(i, []).append(k)
    
  return d

def thesaurus_adv(list):

  seq = []
  
  try:
    for i in list:
      surname = i.split()[1]
      seq += surname[0]
  
    seq = set(seq)
    d = dict.fromkeys(seq)
    
    for i in seq:
      employeers = []
      for k in list:
        surname = k.split()[1]
        if surname[0] == i:
          employeers.append(k)
  
      d[i] = thesaurus(employeers)
      
    return d
  except:
    print("Надо было ввести сотрудников")

if __name__ == "__main__":
  staff = list(input("Введите Имя и Фамилию сотрудников через запятую: ").split(", "))
  print(thesaurus_adv(staff))

