file = 'six_ex/sales.txt'

def main(argv):
  program, *args = argv
  for i in args:
    with open(file,'a',encoding = 'utf-8') as f:
      f.write(i + "\n")

if __name__ == "__main__":
  import sys
  exit(main(sys.argv))