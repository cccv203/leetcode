#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool arithmetic(vector<int> A,int i){
        return (A[i+2] - A[i+1]) == (A[i+1] - A[i]);
    }
    int numberOfArithmeticSlices(vector<int>& A) {
        int ans=0,num=0;
        if(A.size()<3)
            return 0;
        for(int i=0;i<A.size()-2;i++){
            num=0;
            while(arithmetic(A,i)){
                num++;
                i++;
            }
            ans += num*(num+1)/2;
        }
        return ans;
    }
};

int main()
{
    cout << "Hello World!" << endl;
    return 0;
}
