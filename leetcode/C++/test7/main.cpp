#include <iostream>
using namespace std;


int main()
{
    int n;
    scanf("%d",&n);
    float ans=0;
    for(float i=1;i<=n;i++)
        ans += 1/i;
    printf("%f",ans);
}
