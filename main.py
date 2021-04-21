import pyautogui
import keyboard
import win32api, win32con
import time



def clicar(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
time.sleep(2)
while keyboard.is_pressed('space') == False:

    im = pyautogui.screenshot()


    if im.getpixel((738, 500))[0] == 0 and im.getpixel((738, 500))[1] == 0 and im.getpixel((738, 500))[2] == 0:
        clicar(738, 500)
    if im.getpixel((866, 500))[0] == 0 and im.getpixel((866, 500))[1] == 0 and im.getpixel((866, 500))[2] == 0:
        clicar(866, 500)
    if im.getpixel((1007, 500))[0] == 0 and im.getpixel((1007, 500))[1] == 0 and im.getpixel((1007, 500))[2] == 0:
        clicar(1007, 500)
    if im.getpixel((1150, 500))[0] == 0 and im.getpixel((1150, 500))[1] == 0 and im.getpixel((1150, 500))[2] == 0:
        clicar(1150, 500)
        
   




   