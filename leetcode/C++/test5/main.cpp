#include<bits/stdc++.h>
using namespace std;
const int N=100;
int arr[N][N];

int main()
{
    int i,j,k;
    int n,d;
    int sum=0;
    int ans[N][N];
    cin>>n>>d;
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            cin>>arr[i][j];
        }
    }
    int m1 = 0;//横行
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            sum = 0;
            for(k=0; k<d; k++){
                if(j+k>=n) break;
                sum += arr[i][j+k];
            }
            if(m1 < sum){
                m1 = sum;
            }
        }
    }
    //cout<<m1<<endl;
    int m2=0;  //竖列
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            sum = 0;
            for(k=0; k<d; k++){
                if(j+k>=n) break;
                sum += arr[j+k][i];
            }
            if(m2 < sum){
                m2 = sum;
            }
        }
    }
    //cout<<m2<<endl;
    int m3=0;  //左上到右下
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            sum = 0;
            for(k=0; k<d; k++){
                if(i+k>= n ||  j+k >= n) break;
                sum += arr[i+k][j+k];
            }
            if(m3<sum){
                m3 = sum;
            }
        }
    }
    //cout<<m3<<endl;
    int m4=0;  //右上到左下
    for(i=0; i<n-d+1; i++){
        for(j=n-1; j>=0; j--){
            sum = 0;
            for(k=0; k<d; k++){
                if(i+k>=n || j-k<0 ) break;
                sum += arr[i+k][j-k];
            }
            //cout<<sum<<"  ";
            if(m4<sum){
                m4 = sum;
            }
        }
    }
    //cout<<m4<<endl;
    int ma=0;
    ma = max(ma,m1);
    ma = max(ma,m2);
    ma = max(ma,m3);
    ma = max(ma,m4);
    cout<<ma<<endl;
    return 0;
}
