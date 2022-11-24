# TODO
# Написать декоратор, позволяющий валидировать входные значения
# и выбрасывать исключение ValueError, если что-то не так

def val_checker(func):
    def check(x):
        if x >= 0:
            return func(x)
        else:
            raise ValueError(f'wrong val: {x}')

    return check

@val_checker
def calc_cube(x):
    x = x ** 3
    return x

while True:
    a = int(input('Введите число: '))
    print(calc_cube(a))

