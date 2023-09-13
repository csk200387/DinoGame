import curses
import random

def make_feed(height, width, amount=5):
    array = set()
    
    while len(array) != 5:
        array.add(random.randint(height, width), random.randint(height, width))
        





def main(stdscr):
    # 커서 숨김
    curses.curs_set(0)

    # 비동기 모드로 설정
    curses.cbreak()

    # 화면 크기를 얻습니다.
    height, width = stdscr.getmaxyx()

    # "*" 의 위치를 초기화합니다.
    x = width // 2
    y = height // 2

    # 프로그램이 종료될 때까지 반복합니다.
    while True:
        # 화면을 지웁니다.
        stdscr.clear()

        # "*" 를 화면에 그립니다.
        stdscr.addstr(y, x, "🚀")

        # 키보드 입력을 받습니다.
        key = stdscr.getch()

        # 방향키가 눌러졌으면 "*" 의 위치를 이동합니다.
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            if key == curses.KEY_UP:
                y -= 1
            elif key == curses.KEY_DOWN:
                y += 1
            elif key == curses.KEY_LEFT:
                x -= 1
            elif key == curses.KEY_RIGHT:
                x += 1

        # 화면을 업데이트합니다.
        stdscr.refresh()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("Program Stop ")
