from requests import get
from collections import Counter
import os.path
 
arr = []

check_file = os.path.exists('nginx_logs.txt')

if check_file == False:
  res = get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
  with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.write(res.text)

f = open('nginx_logs.txt','r',encoding = 'utf-8')
line = f.readline()
while line:
  a = line.split()
  arr.append(a[0])
  line = f.readline()
  
f.close()

c = Counter(arr).most_common(3)
print(c)