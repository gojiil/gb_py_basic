import requests
import xml.etree.ElementTree as ET

def currency_rates(inp):
  req = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
  
  root = ET.fromstring(req.text)
  
  for i in range(34):
    val = root[i][1].text
    if val == inp:
      kol = root[i][2].text
      summ = root[i][4].text
      print(f"Курс валюты к рублю: {kol} {val} = {summ} RUB")

if __name__ == '__main__':
  need = input("Введите необходимую валюту: ")
  currency_rates(need)