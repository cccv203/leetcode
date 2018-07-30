#include <iostream>
#include<vector>
using namespace std;

class Solution {
public:

    int count(int num){
        int ans=0;
        while(num){
            num&=num-1;
            ans++;
        }
        return ans;
    }

    vector<int> countBits(int num) {
        vector<int> nums;
        for(int i=0;i<=num;i++)
            nums.push_back(count(i));
        return nums;
    }
};

int main()
{
    return 0;
}
