
def type_logger(func):
  def class_wrapper(x):
    for i in range(len(x)):
        print (x[i], type(x[i]))
    markup = func(x)
    return markup

  return class_wrapper




@type_logger
def calc_cube(x):
  for i in range(len(x)):
      x[i] = x[i] ** 3
  return x

a = list(map(int, input('Введите числа через пробел: ').split()))
print(calc_cube(a))
