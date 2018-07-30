#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    int min(int a,int b){
        return a<b?a:b;
    }

    int minimumTotal(vector<vector<int>>& triangle) {
        int len = triangle.size();
        int ans = triangle[0][0];



        for(int i=1;i<len;i++){
            ans=100000;
            for(int j=0;j<=i;j++)
            {
                if(j==0)
                    triangle[i][j] += triangle[i-1][j];
                else if(j==i)
                    triangle[i][j] += triangle[i-1][j-1];
                else
                    triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j]);
                ans = min(ans,triangle[i][j]);
            }
        }
        return ans;

    }
};

int main()
{
    Solution s;
    vector<vector<int>> triangle;
    triangle.push_back(vector<int>{2});
    triangle.push_back(vector<int>{3,4});
    triangle.push_back(vector<int>{6,5,7});
    triangle.push_back(vector<int>{4,1,8,3});

    cout<<s.minimumTotal(triangle);
}
