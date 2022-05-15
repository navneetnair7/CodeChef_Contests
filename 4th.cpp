#include <iostream>
using namespace std;

int main() {
	int t;
    cin >> t;
    for(int i = 0; i < t; i ++){
        int w, x, y, z;
        cin >> w >> x >> y >> z;
        int c = x - w;
        int d = y * z;
        if(c > d) cout << "unfilled" << endl;
        else if(c == d) cout << "filled" << endl;
        else if(c < d) cout << "overflow" << endl;
    }
	return 0;
}
