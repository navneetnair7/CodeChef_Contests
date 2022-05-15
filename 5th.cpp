#include <iostream>
using namespace std;

int main() {
	int t;
    cin >> t;
    for(int i = 0; i < t; i++){
        int n, m;
        cin >> n >> m;
        int a[n];
        for(int j = 0; j < n; j ++){
            cin >> a[j];
        }
        int max = 0;
        for(int j = 0; j < n; j ++){
            for(int k = 0; k < n; k ++){
                int s;
                if((a[j] - a[k]) >= 0) s = a[j] + a[k] + ((a[j] - a[k]) % m);
                else{
                    for(int l = 1; l < 100; l ++){
                        if(m * l >= (a[j] - a[k])){
                            s = a[j] + a[k] + (m * l + (a[j] - a[k]));
                            break;
                        }
                    }
                } 
                if(s > max) max = a[j] + a[k] + ((a[j] - a[k]) % m);
            }
        }
        cout << max << endl;
    }
	return 0;
}