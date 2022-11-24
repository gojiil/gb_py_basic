import os

mem = [10, 20, 30, 40, 50, 100]
mem_d = dict.fromkeys(mem, 0)


root_dir = 'my_project\n'
for root, dirs, files in os.walk(root_dir):
  for d in dirs:
    print(d.replace('\n',''), os.stat(root + '/' + d).st_size)

  for f in files:
    print(f.replace('\n',''), os.stat(root + '/' + f).st_size)

for root, dirs, files in os.walk(root_dir):
  for d in dirs:
    m = os.stat(root + '/' + d).st_size
    if m in range(11):
      mem_d[10] += 1
    elif m in range(11, 21):
      mem_d[20] += 1
    elif m in range(21, 31):
      mem_d[30] += 1
    elif m in range(31, 41):
      mem_d[40] += 1
    elif m in range(41, 51):
      mem_d[50] += 1
    else:
      mem_d[100] += 1

  for f in files:
    m = os.stat(root + '/' + f).st_size
    if m in range(11):
      mem_d[10] += 1
    elif m in range(11, 21):
      mem_d[20] += 1
    elif m in range(21, 31):
      mem_d[30] += 1
    elif m in range(31, 41):
      mem_d[40] += 1
    elif m in range(41, 51):
      mem_d[50] += 1
    else:
      mem_d[100] += 1

print(mem_d)
    
    