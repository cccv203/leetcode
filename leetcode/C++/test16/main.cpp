#include <iostream>

using namespace std;

int arr1[50][50]={0};
int arr2[50] = {0};
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&arr2[i]);
    }

    for(int i=0;i<n;i++)
        for(int j=i+1 ;j<n;j++)
            arr1[i][j] = arr2[i]^arr2[j];

    int ans=0;
    for(int i=0;i<n;i++){
        for(int j=i+1 ;j<n;j++){
            cout<<arr1[i][j]<<'\t';
            if(arr1[i][j]!=0)
                ans++;
            }
        cout<<endl;
    }
    cout<<ans;
}
