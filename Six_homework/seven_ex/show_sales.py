file = 'seven_ex/sales.txt'

def main(argv):
  program, *args = argv
  f = open(file,'r',encoding = 'utf-8')
  if len(args):
    if len(args) > 1:
      lines = f.readlines()[int(args[0]) - 1:int(args[1])]
    else:
      lines = f.readlines()[int(args[0]) - 1:]
  else:
    lines = f.readlines()
    
  f.close()
  for line in lines:
    print(line.replace("\n",""))
    

if __name__ == "__main__":
  import sys
  exit(main(sys.argv))