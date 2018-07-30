#include <iostream>
#include <stdlib.h>
#include <algorithm>
using namespace std;

const int maxn=1e5+10;

struct node
{
    int x,y;
}e[maxn],f[maxn];

int cmp(node a, node b){
    if(a.x==b.x)
        return a.y>b.y;
    return a.x >b.x;
}

int main()
{
    int n, m;
    scanf("%d%d", &n, &m);
    for(int i = 0; i < n; i++) scanf("%d%d", &e[i].x, &e[i].y);
    for(int i = 0; i < m; i++) scanf("%d%d", &f[i].x, &f[i].y);
    sort(e, e + n, cmp);
    sort(f, f + m, cmp);

    int num = 0;
    long long ans = 0;
    int cnt[101];
    for(int i=0;i<101;i++)
        cnt[i]=0;

    //有点像栈
    for(int i =0,j=0;i<m;i++){
        while(j<n && e[j].x>=f[i].x){
                cnt[e[j].y]++;
                j++;
            }
        for(int k=f[i].y;k<=100;k++){
            if(cnt[k]){
                cnt[k]--;
                num++;
                ans += 200*f[i].x + 3*f[i].y;
                break;
            }
        }
    }
    cout<<num<<" "<<ans;

}
