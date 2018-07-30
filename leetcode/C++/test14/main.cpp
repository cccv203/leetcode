#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    long long h;
    scanf("%lld",&h);
    long long i=ceil(sqrt(h))-1;
    for(;;i++){
        if(i*(i+1)>h)
            break;
    }

    cout<<i-1;

}
