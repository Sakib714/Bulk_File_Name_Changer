# Developed by Sadman Sakib
import os


path = 'C:/Users/N.S Computer/OneDrive/Desktop/temp/'   # Path Directory


i=1

for file in os.listdir(path):
    new_name = 'SSS'+str(i)                 # Setting new unique name
    pre_file_name = path + file             # Obj with pre. fila name % directory
    new_file_name = path + new_name         # Obj with new. fila name % directory

    os.rename(pre_file_name, new_file_name) # Renaming Files
    i += 1                                  # Incrementing Value of i



