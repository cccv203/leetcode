#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int repeatedStringMatch(string A, string B) {
        string old_A{A};
        for(int i=1;i<=B.size()/old_A.size()+2;i++){
            if(A.find(B)!=string::npos)
                return i;
            A +=old_A;
        }
        return -1;
    }
};
int main()
{
    Solution s;
    string a{"abc"},b{"cabcabca"};
    cout<<s.repeatedStringMatch(a,b);
}
