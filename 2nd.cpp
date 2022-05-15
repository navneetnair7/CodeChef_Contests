#include <iostream>
using namespace std;

int main() {
	int x, a, b;
    cin >> x;
    cin >> a >> b;
    if(a + b <= x) cout << "Yes";
    else cout << "No";
	return 0;
}
