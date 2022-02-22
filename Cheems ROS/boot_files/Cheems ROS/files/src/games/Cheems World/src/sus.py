import os

list = []

with open('sus.map', 'r') as map:
    for line in map:
        list.append(line.rstrip("\n"))

print(list)

os.system('pause')