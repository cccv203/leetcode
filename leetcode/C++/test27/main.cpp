#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;


class Solution {
public:
    static bool compare(vector<int> a,vector<int> b){
        return a[0]<b[0];
    }

    int findLongestChain(vector<vector<int>>& pairs) {
        int ans=1;
        sort(pairs.begin(),pairs.end(),compare);

        int end = pairs[0][1];
        for (int i = 1; i < pairs.size(); ++i) {
            if (pairs[i][0] > end) {
                ++ans;
                end = pairs[i][1];
            } else if (pairs[i][1] < end) {
                end = pairs[i][1];
            }
        }
        return ans;
    }
};

int main()
{
    Solution s;
    vector<vector<int>> pairs{{-10,-8},{8,9},{-5,0},{6,10},{-6,-4},{1,7},{9,10},{-4,7}};

//    pairs.push_back(vector<int>{1,2});
//    pairs.push_back(vector<int>{3,4});
//    pairs.push_back(vector<int>{2,3});
//    pairs.push_back(vector<int>{2,3});
    cout<<s.findLongestChain(pairs);
    return 0;
}
