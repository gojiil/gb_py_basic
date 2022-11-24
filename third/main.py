from first import num_translate
from second import num_translate_adv
from third import thesaurus
from fourth import thesaurus_adv
from fifth import get_jokes

print("Первое задание:")
word = input("Введите число на английском: ")
print("Перевод:", num_translate(word))

print("*" * 60)

print("Второе задание:")
word = input("Введите число на агнлийском (можно с большой буквы): ")
print("Перевод:", num_translate_adv(word))

print("*" * 60)

print("Третье задание:")
staff = list(input("Введите Имена сотрудников через запятую: ").split(", "))
print(thesaurus(staff))

print("*" * 60)

print("Четвертое задание:")
staff = list(input("Введите Имя и Фамилию сотрудников через запятую: ").split(", "))
print(thesaurus_adv(staff))

print("*" * 60)

print("Пятое задание:")

print(get_jokes(int(input("Введите количество шуток: "))))