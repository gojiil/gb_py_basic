from os import path, makedirs, chdir


l = [0, 0, 0, 0, 0]
folders = [None] * 5


f = open('config.yaml','r',encoding = 'utf-8')

line = f.readline()

while line:
  if "." not in line:
    if line[7] == ' ':
      l[4] += 1
      folders[4] = line.replace(' ', '')
      dir_path = path.join(folders[0], 
                           folders[1], 
                           folders[2], 
                           folders[3], 
                           folders[4])
      if not path.exists(dir_path):
        makedirs(dir_path)
    elif line[5] == ' ':
      l[3] += 1
      folders[3] = line.replace(' ', '')
      dir_path = path.join(folders[0], 
                           folders[1], 
                           folders[2], 
                           folders[3])
      if not path.exists(dir_path):
        makedirs(dir_path)
    elif line[3] == ' ':
      l[2] += 1
      folders[2] = line.replace(' ', '')
      dir_path = path.join(folders[0], 
                           folders[1], 
                           folders[2])
      if not path.exists(dir_path):
        makedirs(dir_path)
    elif line[1] == ' ': 
      l[1] += 1
      folders[1] = line.replace(' ', '')
      dir_path = path.join(folders[0], 
                           folders[1])
      if not path.exists(dir_path):
        makedirs(dir_path)
    else:
      l[0] += 1
      folders[0] = line
      dir_path = path.join(folders[0])
      if not path.exists(dir_path):
        makedirs(dir_path)
  else:
    text_file = open(dir_path + "/" + line.replace(' ',''), "w")
    text_file.close()

  line = f.readline()

f.close()
print(l)
