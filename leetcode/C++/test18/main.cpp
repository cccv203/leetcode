#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int min(int m,int n){
        return n>m?m:n;
    }


    int minCostClimbingStairs(vector<int>& cost) {
        cost.push_back(0);
        int n = cost.size();
        int arr[1002] = {0};
        arr[1] = cost[0];
        for(int i=1;i<n;i++){
            arr[i+1] = min(arr[i]+cost[i], arr[i-1]+cost[i]);
        }
        return arr[n];
    }
};
