import time
import pyautogui as pag

def sleep(r):
    time.sleep(r)
    return

def hold():
    pag.mouseDown(button='right')
    sleep(100)
    pag.mouseUp(button='right')
    return
loop=1

while (loop>0):
    print(loop)
    pag.click(button="right")
    sleep(5)
    loop=loop+1
    sleep (100)
