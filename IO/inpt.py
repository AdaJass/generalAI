import win32gui
from PIL import ImageGrab
import win32con
import time

__hwnd = win32gui.FindWindow(0,"天涯明月刀")
if not __hwnd:
    print('window not found!')
    exit()

win32gui.SetForegroundWindow(__hwnd)
win32gui.ShowWindow(__hwnd, win32con.SW_RESTORE)  
__game_rect = win32gui.GetWindowRect(__hwnd)

input('waiting for running!')
__adj_game_rect = (__game_rect[0] +5, __game_rect[1] + 35, __game_rect[2]-5, __game_rect[3]-10)
def getScreen():
    src_image = ImageGrab.grab(__adj_game_rect)
    return src_image

if __name__ == '__main__':
    getScreen()
