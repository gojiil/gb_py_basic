from requests import get
import os.path

def kort (st):
  ar = st.split()

  a = ar[0]
  b = ar[5].lstrip('"')
  c = ar[6]
  kor = (a, b, c)
  arr.append(kor)
  
arr = []

check_file = os.path.exists('nginx_logs.txt')

if check_file == False:
  res = get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
  with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.write(res.text)

f = open('nginx_logs.txt','r',encoding = 'utf-8')
line = f.readline()
while line:
  kort(line)
  line = f.readline()
  
f.close()


print(arr)