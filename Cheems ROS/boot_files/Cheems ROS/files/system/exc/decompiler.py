"""

CheemsHeaders : 


appdata = ['name', 'version']
metadata = ['preftime', 'dir']

title = '%CD%'

Code : 

write Hello World

"""

import base64, modified_shell, os
from datetime import datetime

default_headers = ''
name_application = ''
version = ''
intigerlimit = 25000

def decompile(name):
    global version, name_application, intigerlimit

    # VARIABLES

    Code = False
    BatchAssembled = False
    OutputCode = []
    BatchCode = []
    OutputCodeString = ''

    # GET CODE

    with open(name, mode='rb') as file:
        compiled_data = file.read()

    print(compiled_data)

    compiled_data = base64.b64decode(compiled_data)

    for line in compiled_data.splitlines():
        line = line.decode()
        print(line)

        if Code == True:
            OutputCode.append(line)
        if 'Code :' in line[0:6]:
            BatchAssembled = False
            Code = True
        if BatchAssembled == True:
            BatchCode.append(line)
        if 'Batch Assembled :' in line[0:17]:
            BatchAssembled = True

    for obj in OutputCode:
        OutputCodeString += obj + '\n'


    # COMPILE WITH SHELL

    os.system('cls')

    for line in BatchCode:
        if line != '\n':
            if "cd " in line[0:3]:
                line = str(line[0:intigerlimit])
                line = line.replace("cd ", "")
                os.chdir(line)
            else:
                os.system(line)
            