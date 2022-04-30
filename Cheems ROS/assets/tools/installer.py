import os

os.system('title Cheems Dependencies Installer')

dependencies = []

os.system('cls')

print('Preparing dependencies...')

os.system("pip install tqdm -q")

os.system('cls')

from tqdm import tqdm

with open('dependencies.txt','r') as f: dependencies = f.readlines(); f.close()

for i in tqdm(dependencies,'Installing Dependencies',colour='green'):
    if 'uninstall' in i:
        print(f"\nCurrently Installing: (patching){i.replace('pip uninstall','').replace('-y','').replace('-q','')}")
    elif '==' in i:
        print(f"\nCurrently Installing: {i.replace('pip install','').replace('-q','').replace('==1.2.2','').replace(' ','')}")
    else:
        print(f"\nCurrently Installing: {i.replace('pip install','').replace('-q','').replace(' ','')}")
    os.system(i)
    os.system('cls')

print('\nAll Packages (now) Are Installed!')

os.system('pause >nul')