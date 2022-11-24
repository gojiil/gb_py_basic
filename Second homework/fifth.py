from random import random

prices = []
price = ""

for i in range(20):
  prices.append(round(random()*100,2))
  prices[i] = str(int(prices[i])).zfill(2) + " руб. " + str(int((prices[i]%1)*100)).zfill(2) + " коп."

print (", ".join(prices))