import os
from shutil import copy

root_dir = 'my_project\n'
for root, dirs, files in os.walk(root_dir):
  for i in files:
    if '.html' in i:
      old = root + '/' + i
      
      root_dir = root.split('\n')
      for k in range(1, len(root_dir)):
        if root_dir[k-1] == '/templates':
          dir_path = 'my_project\n/templates\n/' + root_dir[k] + '\n'
          if not os.path.exists(dir_path):
            os.makedirs(dir_path)
      
      new = dir_path + '/' + i
      copy(old, new)
