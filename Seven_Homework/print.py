import os

root_dir = 'my_project\n'
for root, dirs, files in os.walk(root_dir):
  path = root.split(os.sep)
  print((len(path)-1) * "  |" + "--" + os.path.basename(root.replace("\n","")))
  for file in files:
    print(len(path) * "  |" + "--" +  file.replace("\n",""))
