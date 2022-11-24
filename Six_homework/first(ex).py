from requests import get

arr = []

res = get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

result = res.text.split("\n")

def kort (st):
  ar = st.split()

  a = ar[0]
  b = ar[5].lstrip('"')
  c = ar[6]
  kor = (a, b, c)
  arr.append(kor)

for i in range(len(result)-1):
  kort(result[i])

print(arr)