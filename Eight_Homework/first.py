# TODO
# 1. написать функцию emial_parse(address) которая извлекает имя пользователя
# и домен в словарь {'username': 'name', 'domain':'domain'}
# если домен неликвиден, возвращает ошибку ValueError

import re

RE_ADDRESS = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+(?:[.]\w+))$')

def address_is_valid(address):
    return RE_ADDRESS.match(address)


address = input('input e-mail address:\n')
while True:
    if address_is_valid(address):
        print(address_is_valid(address).groupdict())
        address = input('input e-mail address:\n')
    else:
        raise ValueError(f'Is not email address: {address}')

