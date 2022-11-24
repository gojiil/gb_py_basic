list = ["инженер-конструктор Игорь","главный бухгалтер МАРИНА","токарь высшего разряда нИКОЛАй","директор аэлита"]

for i in list:
  name = i.split()[-1:]
  name = str(name[0])

  a = ("".join(name[:1])).upper()
  b = ("".join(name[1:])).lower()

  name = a + b
  print(f"Привет, {name}!")