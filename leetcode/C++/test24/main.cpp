#include <iostream>
#include <string>
using namespace std;


class Solution {
public:

    int countSubstrings(string s) {
        int len = s.size();
        int arr[1001][1001];
        for(int i=0;i<len;i++)
            arr[i][i] = 1;

        for(int i=len-2;i>=0;i--){
            for(int j=i+1;j<len;j++){
                if(s[j]!=s[i])
                    arr[i][j] = arr[i+1][j] + arr[i][j-1] - arr[i+1][j-1];
                else{
                    arr[i][j] = arr[i+1][j] + arr[i][j-1] +1;
                }
            }
        }
        return arr[0][len-1];
    }

};

int main()
{
    string s{"fdsklfa"};
//    cin>>s;
    Solution sss;
    cout<<sss.countSubstrings(s);
    return 0;
}
