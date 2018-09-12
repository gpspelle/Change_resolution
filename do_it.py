import os

classes = ['Falls/', 'NotFalls/']
path = 'teste_FDD'

for c in classes:
    for folder in os.listdir(path + c): 
        print(folder)
        command = 'python3 change_resolution.py -path ' + path + c + folder + '/' + folder + '.mp4' + ' -res 224 224'
        os.system(command)

