tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена', 'Борис', 'Станислав'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

def Generator():
  for i in range(len(tutors)):
    try:
      child = (tutors[i], klasses[i])
    except IndexError:
      child = (tutors[i], None)
    yield child

mygen = Generator()

for tuple_child in mygen:
  print(tuple_child)
