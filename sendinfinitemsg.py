import pyautogui as pg
import time 

time.sleep(10)

for i in range(100):
    pg.write("helo")
    pg.press('Enter')
