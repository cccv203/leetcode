#include <iostream>

using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        int arr[101][101] = {0};
        for(int i=1;i<101;i++){
            arr[i][0] = 1;
            arr[0][i] = 1;
        }

        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++)
                arr[i][j] = arr[i-1][j] + arr[i][j-1];
        }
        return arr[m-1][n-1];
    }
};
int main()
{
    cout << "Hello World!" << endl;
    return 0;
}
