import os
path = os.getcwd()
print(path)
folder = 'sample'
whole_path = os.path.join(path,folder,'new1','new2')
print(whole_path)
#os.mkdir(whole_path)  #create single folder
#os.makedirs(whole_path) #create multiple
print(os.listdir(path))



#
#
# os.mkdir('C:\\Users\dines\PycharmProjects\pythonProject2\sample')



