import os   #operating system
path = os.getcwd() #current working dir
print('path: ',path)
new_folder = 'dinesh'
print('new_folder:',new_folder)
whole_path = os.path.join(path,new_folder)
print('whole_path using join func',whole_path)
try:
    os.mkdir(whole_path) # to create new folder
except:
    print('file already exists')
os.rmdir(whole_path)