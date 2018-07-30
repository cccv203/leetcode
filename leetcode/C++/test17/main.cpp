#include <iostream>
#include <vector>

using namespace std;

class NumArray {
public:
    vector<int> num;
    NumArray(vector<int> nums) {
        for( auto it=nums.begin(); it<nums.end(); it++)
            num.push_back(*it);
    }

    int sumRange(int i, int j) {
        int ans=0;
        for(int k=i;k<=j;k++)
            ans += num[k];
        return ans;
    }
};

int main(){
    return 0;
}
/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */
