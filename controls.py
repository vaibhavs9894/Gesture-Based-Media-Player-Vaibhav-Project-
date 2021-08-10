import pyautogui as pg
import time
sw, sh = pg.size()

def activate_right_software():
    pg.moveTo(x=sw//2+300,y=sh//2)
    pg.click()

def activate_left_software():
    pg.moveTo(x=sw//3,y=sh//2,duration=2)
    pg.click()

def play_or_pause():
    pg.press('space')
    time.sleep(2)

def volume_up():
    pg.press('up')

def volume_down():
    pg.press('down')


def forward():
    pg.press('right')

def backward():
    pg.press('left')
