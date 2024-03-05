import pyautogui
import keyboard
import time

start_num = 36

print("10초 후 매크로 시작")
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("마우스를 움직이지 마세요. esc를 꾹누르면 종료됩니다.")

while keyboard.is_pressed('esc') == False:
    try:
        pyautogui.rightClick(pyautogui.position())
        # 6회

        for i in range(6):
            pyautogui.press('down')
        pyautogui.press('enter')

        pyautogui.write(str(start_num).zfill(3))
        pyautogui.press('enter')

        start_num += 1
        time.sleep(1)
    except KeyboardInterrupt:
        print("프로그램 종료")
        print("마지막 번호: ", start_num)
        break
