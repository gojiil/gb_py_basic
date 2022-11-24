dict = {
  "one":"один",
  "two":"два",
  "three":"три",
  "four":"четыре",
  "five":"пять",
  "six":"шесть",
  "seven":"семь",
  "eight":"восемь",
  "nine":"девять",
  "ten":"десять",
  "zero":"ноль",
}


def num_translate_adv(input_word): 

  try:
    for i in dict:
      if input_word.istitle():
        if input_word.lower() == i:
          result = dict[i].capitalize()
          
      else:
        if input_word.lower() == i:
          result = dict[i]
    
    return result

  except:
    pass

if __name__ == "__main__":
  word = input("Введите число от 0 до 10 на английском: ")
  print("Перевод:",num_translate_adv(word))




  