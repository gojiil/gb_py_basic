#TODO - Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):

from random import randint



def get_jokes(count):

  nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
  adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
  adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

  jokes = []
  while count:
    try:  
      joke = ""
      num = randint(0, len(nouns)-1)
      joke += nouns.pop(num) + " "
      num = randint(0, len(adverbs)-1)
      joke += adverbs.pop(num) + " "
      num = randint(0, len(adjectives)-1)
      joke += adjectives.pop(num)
  
      jokes.append(joke)
      count -= 1

    except ValueError:
      count = 0

  return jokes

if __name__ == "__main__":
  print(get_jokes(int(input())))
    
  