//파이썬으로는 시간초과 뜸
#include <iostream> 
#define MAX 20
using namespace std;

int R, C,ans;
char arr[MAX][MAX];
bool alpha[26];

int x_list[] = { 0,0,-1,1 };
int y_list[] = { -1,1,0,0 };

void Input() {
	cin >> R >> C;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cin >> arr[i][j];
		}
	}
}

int bigger(int a, int b) {
	if (a > b)
		return a;
	return b;
}

void back(int x, int y, int count) {
	ans = bigger(ans, count);

	for (int i = 0; i < 4; i++) {
		int go_x = x + x_list[i];
		int go_y = y + y_list[i];

		if (0 <= go_x && go_x < C && 0 <= go_y && go_y < R) {
			int check = arr[go_y][go_x] - 'A';
			if (!alpha[check]) {
				alpha[check] = true;
				back(go_x, go_y, count + 1);
				alpha[check] = false;
			}
		}
	}

}

int main(void) {
	Input();
	alpha[arr[0][0] - 'A'] = true;
	back(0, 0, 1);
	cout << ans;
}
