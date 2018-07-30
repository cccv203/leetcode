#include <iostream>
#include <algorithm>
using namespace std;
bool compare(int a,int b)
{
  return a>b; //升序排列，如果改为return a>b，则为降序
}
int main()
{
    int nums,ans=0;
    scanf("%d",&nums);
    int arr[nums];
    for(int i=0;i<nums;i++)
        scanf("%d",&arr[i]);
    if(nums%2!=0){
        nums++;
        arr[nums]=0;
    }
    sort(arr,arr+nums,compare);
    for(int i=1;i<nums;i++,i++)
        ans += arr[i-1] - arr[i];
    cout<<ans;
}
