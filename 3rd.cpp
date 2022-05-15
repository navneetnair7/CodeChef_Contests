#include <iostream>
using namespace std;

int main() {
	int t;
    cin >> t;
    for(int i = 0; i < t; i++){
        int n;
        cin >> n;
        int d[n];
        for(int j = 0; j < n; j++){
            cin >> d[j];
        }
        int count = 0;
        for(int k = 0; k < n; k ++){
            if (d[k] >= 1000) count ++;
        }
        cout << count << endl;
    }
	return 0;
}
