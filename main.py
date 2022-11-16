from PIL import ImageGrab
import pyautogui
import time
import Xlib
import win32api
import win32gui

def win(n) : # Windows
    for i in range(1,n+1) :
        start = time.time()
        stack = 0
        pyautogui.moveTo(300,328)
        pyautogui.click()
        while True :
            screen = win32gui.GetDC(win32gui.GetActiveWindow())
            if win32gui.GetPixel(screen, 300, 328) == 0x535353 :
                #print("jump")
                #pyautogui.press('space')
                pyautogui.keyDown('up')
                pyautogui.keyUp('up')
                stack += 1

            elif win32gui.GetPixel(screen, 389, 248) == 0x535353 :
                #print("ohh,,,,")
                print("jump =",stack)
                print("try =",i)
                print("time :", time.time() - start)
                pyautogui.moveTo(1100,500)
                pyautogui.click()
                break;


def li() : # Ubuntu
    for _ in range(100000000) :
        screen = ImageGrab.grab()
        if screen.getpixel((352, 356)) == (83, 83, 83) :
            pyautogui.press("up")
            print("Jump!")
        if screen.getpixel((572, 262)) == (83, 83, 83) :
            print("ohh,,,")
            break;

def getScreenPixel() :
    for i in range(1000) :
        time.sleep(0.5)
        screen = ImageGrab.grab()
        po = pyautogui.position()
        print(po)
        print(screen.getpixel((po)))

 
if __name__ == "__main__" :
    pyautogui.moveTo(352, 356)
    pyautogui.click()
    li()
    #getScreenPixel()
