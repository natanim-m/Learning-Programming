#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	freopen("fence.in", "r", stdin);
	freopen("fence.out", "w", stdout );
	int N;
	cin >> N;
	vector<int> diff(102,0);
	int max_R = 0;
	for (int i = 0; i < N; i++) {
		int L, R, V;
		cin >> L >> R >> V;
		diff[L] += V;
		diff[R+1] -= V;
		max_R = max(max_R, R);
	}
	int running_noise = 0;
	int max_noise = 0;
	for(int j = 1; j <= max_R; j++) {
		running_noise += diff[j];
		if(max_noise < running_noise) { max_noise = running_noise; }
	}
	cout << max_noise << "\n";
	return 0;
}