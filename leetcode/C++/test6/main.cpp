#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int n=1;
//    scanf("%d",&n);
    cout<<"hello"<<endl;

    long long c[1000][1000];
    c[0][0] = 1;
    for(int i = 1; i <= 100; i++) {
        c[i][0] = 1;
        for(int j = 1; j <= 100; j++)
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]);
    }
    int ans=0;
    for(int i=0;i<n/2-1;i++)
        ans += (1+n)*c[n-1][n-1+i];
    if(n%2!=0)
        ans += int((n+1)/2)*c[n-1][int((n-1)/2)];
    printf("%.4f",float(ans/pow(2,n-1)));
}
