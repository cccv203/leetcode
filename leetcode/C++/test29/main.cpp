 #include <iostream>

using namespace std;
int handle(int a,int b) {
        if(a==0) return b;
        if(b==0) return a;
        int i=a^b;
         int j=(a&b)<<1;
        return  handle(i,j);
    }
int main()
{
    cout<<handle(1024,256);

}
