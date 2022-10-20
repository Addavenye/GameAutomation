import pyautogui as pag
import sys
import time

print(pag.size())
#global values
x=0
pag.moveTo(1000, 330)
handx = 1066
handy = 735
colomn1 = 750
colomn2 = 800
row1 = 550
row2 = 600
row3 = 650
d='d'
s='s'
w='w'
a='a'

def sleep(s=0):
    time.sleep(s)
    return

def bag2hand(x=0,y=0,x2=0,y2=0):
    ##pickup
    pag.moveTo(x2,y2,.5)
    pag.click()
    ##drop to hand
    pag.moveTo(x,y,.5)
    pag.click()
    ##drop to bag
    pag.moveTo(x2,y2,.5)
    pag.click()
    return

def plant(plot,d1,d2):
    l=0
    pag.press('7')
    pag.press('f')
    pag.press('6')
    while(l!=plot):
        pag.keyDown(d1)
        sleep(0.06)
        pag.keyUp(d1)
        pag.click()
        pag.click(button='right')
        pag.click(button='right')
        l=l+1
    pag.keyDown(d2)
    sleep(0.065)
    pag.keyUp(d2)
    
    return
def plantloop(plot,d,a,s):
    x=0
    while(x<plot):
        plant(plot,d,s)
        plant(plot,a,s)
        x=x+1
    return
##  0 ----> 1920
##  |
##  v
##  1080

loop=1
try:
    while (loop>0):
        x, y = pag.position()
        POS = 'X - ' + str(x).rjust(4) + ' Y - ' + str(y).rjust(4)
        print (POS)
        time.sleep(1)
        bag2hand(handx,handy,colomn1,row1)
        #bag2hand(handx,handy,colomn1,row2)
        #bag2hand(handx,handy,colomn1,row3)
        #bag2hand(handx,handy,colomn2,row1)
        #bag2hand(handx,handy,colomn2,row2)
        #bag2hand(handx,handy,colomn2,row3)
        pag.press('e')
        plantloop(9,d,a,s)
        print(loop)
        loop=loop+1
        sleep(10)
except KeyboardInterrupt:
    print('\n')
    ##1000, 330
##move and click above
