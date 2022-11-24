# TODO
# Написать регулярное выражение для парсинга файла логов
# web-сервера из ДЗ 6 урока nginx_logs.txt
from requests import get
import re

RE_RAW = re.compile(r'(\S+)\D[^[]+(\S+\s\S+)\s\"(\S+)\s(\S+)\s\S+\s(\d+)\s(\d+)')

def raw_is_valid(raw):
    return RE_RAW.match(raw)


request = get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

request = request.text.split('\n')

for i in range(len(request) - 1):
    if raw_is_valid(request[i]):
        print(RE_RAW.findall(request[i]))
    else:
        raise ValueError(f'Is not valid raw: {request[i]}')
