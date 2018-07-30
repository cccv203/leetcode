#include <iostream>

using namespace std;

class Solution {
public:
    int max(int a,int b, int c,int d, int e){
        a = a>b?a:b;
        a = a>c?a:c;
        a = a>d?a:d;
        a = a>e?a:e;
        return a;
    }

    int integerBreak(int n) {
        int arr[100] = {0};
        for(int i=2;i<=n;i++){
            for(int j=1;j<i;j++)
                arr[i] = max(j*(i-j),j*arr[i-j],arr[j]*(i-j),arr[j]*arr[i-j],arr[i]);
        }
        return arr[n];

    }
};

int main()
{
    Solution s;
    cout<<s.integerBreak(5);
}
