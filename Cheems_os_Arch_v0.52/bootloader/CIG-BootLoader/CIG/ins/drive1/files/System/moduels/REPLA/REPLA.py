import os

os.chdir("..")
os.chdir("..")

with open('mn_col.$', 'r') as r:
    repl = r.read().replace('\n', '').replace(' ', '')

fp = open('mn_col.$', 'w')
fp.write(repl)
fp.close()

quit()