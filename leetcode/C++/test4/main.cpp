#include <iostream>
#include <string>
using namespace std;
int main() {
    int i = 0, n = 1;
    string a;
    string b;
    cin >> a;
    while (a[i]) {
        if (a[i + 1] == a[i]) {
            n++;
        }
        else {
            cout << n << a[i];
            n = 1;
        }
        i++;
    }
    return 0;
}
