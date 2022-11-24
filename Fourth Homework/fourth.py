from utils import currency_rates

while True:
  need = input("Введите необходимую валюту: ").upper()
  try: 
    k, v, s = currency_rates(need)
    print (f"Курс валюты к рублю: {k} {v} = {s} RUB")
    print("*" * 60)
  except Exception:
    break

print("Выход из программы!") 
