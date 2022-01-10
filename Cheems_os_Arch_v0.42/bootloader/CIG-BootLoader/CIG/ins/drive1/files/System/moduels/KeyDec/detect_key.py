from pynput.keyboard import Key, Listener
  
def show(key):
  
    with open('cur_key.txt', 'w') as f:
        f.write('{0}'.format( key))
  
# Collect all event until released
with Listener(on_press = show) as listener:   
    listener.join()