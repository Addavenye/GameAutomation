#holds down mouse button (can do left or right click)
import pyautogui as pag
import sys
import time

def sleep(s=0):
    time.sleep(s)
    return

def hold():
    pag.mouseDown(button='right')
    sleep(100)
    pag.mouseUp(button='right')
    return
def holdl():
    pag.mouseDown()
    sleep(100)
    pag.mouseUp()
    return
loop=1

while (loop>0):
    sleep(5)
    print('down')
    #change this between hold() and holdl()
    hold()
    print('up')
    print(loop)
    sleep(5)
    print("10 seconds")
    loop=loop+1
