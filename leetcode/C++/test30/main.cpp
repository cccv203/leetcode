#include <iostream>

using namespace std;

int main()
{
    int a,b,c;
    scanf("%d%d%d",&a,&b,&c);
    if(a!=b & b!=c & a!=c)
        cout<<a+b+c+3<<endl;
    if(a!=b & b==c)
        cout<<a+2+(b>1?b:1)<<endl;
    if(a!=c & b==a)
        cout<<c+2+(a>1?a:1)<<endl;
    if(c!=b & a==c)
        cout<<b+2+(a>1?a:1)<<endl;
    if(a==b & a==c){
        if(a==0)
            cout<<3<<endl;
        if(a==1)
            cout<<4<<endl;
        if(a==2)
            cout<<3<<endl;
        if(a>2)
            cout<<a+1<<endl;
    }
    return 0;
}
