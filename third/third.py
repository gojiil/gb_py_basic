
def thesaurus(list):

  seq = []
  d = dict()

  try:
    for i in list:
      seq += i[0]
  
    seq = set(seq)
    
    for i in seq:
      for k in list:
        if k[0] == i:
          d.setdefault(i, []).append(k)
    
    return d
  except:
    print("Надо было ввести сотрудников")
    
  

if __name__ == "__main__":
  staff = list(input("Введите Имена сотрудников через запятую: ").split(", "))
  print(thesaurus(staff))
