#include <stdlib.h> // 난수생성
#include <termios.h> // gcc용 키보드 이벤트
#include <stdio.h> // printf
#include <time.h> // 난수를 랜덤하게

int getch() { // gcc컴파일러 키보드 이벤트 윈도우는 알잘딱으로 수정하시길
	int c;
	struct termios oldattr, newattr;

	tcgetattr(STDIN_FILENO, &oldattr);           // 현재 터미널 설정 읽음
	newattr = oldattr;
	newattr.c_lflag &= ~(ICANON | ECHO);         // CANONICAL과 ECHO 끔
	newattr.c_cc[VMIN] = 1;                      // 최소 입력 문자 수를 1로 설정
	newattr.c_cc[VTIME] = 0;                     // 최소 읽기 대기 시간을 0으로 설정
	tcsetattr(STDIN_FILENO, TCSANOW, &newattr);  // 터미널에 설정 입력
	c = getchar();                               // 키보드 입력 읽음
	tcsetattr(STDIN_FILENO, TCSANOW, &oldattr);  // 원래의 설정으로 복구
	return c;
}

int score = 0;
int arr[10]; // 랜덤좌표 저장할 배열. 마땅한 자료형을 못찾음

int feedPosi() { // 먹이 위치 선정
	srand(time(0));
	for (int i = 0; i < 10; i++) {
		if (i%2==0) arr[i] = rand()%80;	// i가 짝수일 때 x좌표
		else arr[i] = rand()%20;	// i가 홀수일 때 y좌표
	}
}

int eat(int x, int y) { //시야에서 없애버리는 함수
	arr[x] = 80; 
	arr[y] = 20;
	score += 20;
	printf("@");
}

/** x, y 좌표 입력 받은 후 게임 보드 생성 */
int print_matrix(int x, int y) {
	system("clear");
	for (int i = 0; i < 20; i++) {
		for (int l = 0; l < 80; l++) {

			if (i == arr[1] && l == arr[0]) {
				if (x == arr[0] && y == arr[1]) eat(1,0);
				else printf("*");
			}
			else if (i == arr[3] && l == arr[2]) {
				if (x == arr[2] && y == arr[3]) eat(3,2);
				else printf("*");
			}
			else if (i == arr[5] && l == arr[4]) {
				if (x == arr[4] && y == arr[5]) eat(5,4);
				else printf("*");
			}
			else if (i == arr[7] && l == arr[6]) {
				if (x == arr[6] && y == arr[7]) eat(7,6);
				else printf("*");
			}
			else if (i == arr[9] && l == arr[8]) {
				if (x == arr[8] && y == arr[9]) eat(9,8);
				else printf("*");
			}
			else if (i == y && l == x) printf("@");
			else printf(" ");

		}
		printf("\n");
	}
	printf("================================================================================\n");
}

int main() {
	feedPosi();
	char c;
	int x = 40;
	int y = 10;
	print_matrix(x,y);
	printf("i, k, j, l로 이동 가능\n");
	while (1) {
		c = getch();
		if (c == 'i') y--;
		if (c == 'k') y++;
		if (c == 'j') x--;
		if (c == 'l') x++;
		print_matrix(x,y);
		printf("total score = %d\n", score);
		if (score == 100) break;
	}
	printf("congratulation\n");
}
