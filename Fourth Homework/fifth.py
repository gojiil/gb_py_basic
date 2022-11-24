from utils import currency_rates

def main(argv):
  program, *args = argv
  for i in args:
    i = i.upper()
    try: 
      k, v, s = currency_rates(i)
      print (f"Курс валюты к рублю: {k} {v} = {s} RUB")
      print("*" * 60)
    except Exception:
      continue 

if __name__ == '__main__':
  import sys

  if sys.argv == ['main.py']:
    list = ['main.py']
    list += input("Введите необходимые валюты через пробел: ").split()
    main(list)

  else:
    exit(main(sys.argv))
    
  print("Выход из программы!") 
  