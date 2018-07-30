#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int arr[1001] = {1};
        queue<vector<int>> que;
        que.push(vector<int>{rooms[0]});
        while (que.size()) {
            vector<int>temp{que.front()};
            que.pop();
            for(int i=0;i<temp.size();i++){
                if(!arr[i]){
                    arr[i]=1;
                    que.push(vector<int>{rooms[i]});
                }
            }
        }
        for(int i=0;i<rooms.size();i++)
            if(!arr[i])
                return false;
        return true;

    }
};

int main()
{
    cout << "Hello World!" << endl;
    return 0;
}
