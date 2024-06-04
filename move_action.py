import pyautogui
import time

class Move_Action():
    def __init__(self,sleep=0.5):
        self.sleep = sleep

    def move(self, coord):
        pyautogui.moveTo(coord[0],coord[1])
        time.sleep(self.sleep)
    
    def s_click(self, coord):
        self.move(coord)
        pyautogui.click(button='left')
        time.sleep(self.sleep)
    
    def d_click(self,coord,delay=0.2):
        self.move(coord)
        pyautogui.click(button='left')
        time.sleep(delay)
        pyautogui.click(button='left')
        time.sleep(self.sleep)
    
    def write(self,coord,message=str,delay=0.2):
        self.d_click(coord)
        pyautogui.write(message, interval=delay)

if __name__ == '__main__':
        action = Move_Action(1)
        