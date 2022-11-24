# Не придумал, как реализовать так, чтобы читал не количество символов, а строку
# Поэтому пока что можно вводить только 6-зн числа 

file = 'seven_ex/sales.txt'

def main(argv):
  program, knt, nom = argv
  try:    
    with open(file,'r+',encoding = 'utf-8') as f:
      f.seek(0,2)
      last = f.tell()
      knt = 7*(int(knt) - 1)
      if last >= knt:
        f.seek(knt,0)
        f.write(nom + "\n")
      else:
        print("Такого не существует")
  except IOError:
    print("Файла не существует")

if __name__ == "__main__":
  import sys
  exit(main(sys.argv))