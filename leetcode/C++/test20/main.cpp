#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    int min(int a,int b){
        return a<b?a:b;
    }



    int minPathSum(vector<vector<int>>& grid) {
        if(grid.size()==0||grid[0].size()==0)
            return 0;
        int m=grid.size(),n=grid[0].size();
        int arr[1000][1000] = {0};
        for(int i=2;i<m+1;i++)
            arr[i][0] = 1000;
        for(int i=2;i<n+1;i++)
            arr[0][i] = 1000;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                arr[i+1][j+1] = min(arr[i+1][j]+grid[i][j], arr[i][j+1]+grid[i][j]);
                cout<<arr[i+1][j+1]<<'\t';
            }
            cout<<endl;
        }
        return arr[m][n];
    }
};

int main()
{
    vector<vector<int>> grid = {vector<int>{1,3,1},vector<int>{1,5,1},vector<int>{4,2,1}};
    Solution s;
    cout<<s.minPathSum(grid);
}
