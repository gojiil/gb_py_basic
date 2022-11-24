import os

main_folder = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for i in folders:
  dir_path = os.path.join(main_folder, i)
  if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    


