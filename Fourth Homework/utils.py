import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def currency_rates(inp):
  req = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
  
  root = ET.fromstring(req.text)
  
  for i in range(34):
    val = root[i][1].text
    if val == inp:
      kol = root[i][2].text
      summ = root[i][4].text

      dat = root.attrib['Date']
      dat = datetime.strptime(dat,"%d.%m.%Y")
      print("Дата:",dat.date())
      break
      
  return kol, val, summ

  