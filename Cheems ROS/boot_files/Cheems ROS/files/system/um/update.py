import um, requests, os, progressbar, hashlib

url = 'http://ros.pythonanywhere.com/update'
varBar = ''
PrgBar = ''

def Spin_Spinner():
    global varBar
    
    varWidget = ['Getting Update From Server ', progressbar.AnimatedMarker()]
    varBar = progressbar.ProgressBar(widgets = varWidget).start()

def update():
    global varBar
    varBar.update()

def Update_Progessbar():
    global PrgBar
    
    widgets = [progressbar.Timer(format= '  Downloading Update'),
             ' : ',
               progressbar.Bar('█')
              ]
      
    PrgBar = progressbar.ProgressBar(max_value=200, 
                                  widgets=widgets).start()

Spin_Spinner()
update()

local_filename = url.split('/')[-1]
with requests.get(url, stream=True) as r:
    r.raise_for_status()
    update()
    with open('UPDATE.zip', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

hashlib.md5().update(chunk)
digest = hashlib.md5().hexdigest()


if os.path.exists('LAST_UPDATE.zip'):

    with open('LAST_UPDATE.zip', 'wb') as f:
        hashlib.md5().update(chunk)
        digest_lst = hashlib.md5().hexdigest()

    if digest_lst == digest:
        print('   System Up To Date')
        quit()
            
update()

varBar.finish()

Update_Progessbar()

if os.path.exists('UPDATE.zip'):
    um.decomp('UPDATE.zip')
    PrgBar.update(20)
    um.ignore('ignore.txt',desc=False)
    PrgBar.update(20)
    um.updatefile('Update',desc=False)
    PrgBar.update(10)
    ver = um.InstallUpdate(desc=False)
    PrgBar.update(40)
else:
    print('ERROR Could Not Get Update From Server')
    quit()
PrgBar.finish()

os.system('rename UPDATE.zip, LAST_UPDATE.zip')

print('Successfully Installed Update', ver[0])
