#include <iostream>
#include <string>
using namespace std;


class Solution {
public:
    int min(int a,int b){
        return a<b?a:b;
    }

    int minimumDeleteSum(string s1, string s2) {
        int len1=s1.size(),len2=s2.size();
        int arr[1001][1001] = {0};
        for(int i=0; i<len1;i++)
            arr[i+1][0] = arr[i][0]+char(s1[i]);
        for(int i=0; i<len2;i++)
            arr[0][i+1] = arr[0][i]+char(s2[i]);

        for(int i=0;i<len1;i++){
            for(int j=0;j<len2;j++){
                if(s1[i] == s2[j]){
                    arr[i+1][j+1] = arr[i][j];
                }
                else
                    arr[i+1][j+1] = min(arr[i][j+1] + char(s1[i]), arr[i+1][j] + char(s2[j]));
            }
        }
        return arr[len1][len2];
    }
};

int main()
{
    cout << "Hello World!" << endl;
    return 0;
}
