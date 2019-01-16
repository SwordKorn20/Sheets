from libs import globals

f = open(globals.file_name, 'r')

for line in f:
    print(line)
