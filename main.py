import os


path = 'C:/Users/N.S Computer/OneDrive/Desktop/temp/'
i=1
for file in os.listdir(path):
    new_name = 'SSS'+str(i)
    pre_file_name = path + file
    new_file_name = path + new_name
    os.rename(pre_file_name, new_file_name)
    i += 1



