#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool cmp(char a,char b){
    return a>b;
}
int main()
{
    string s,t;
    cin>>s>>t;
    sort(t.begin(),t.end(),cmp);
    for(int i=0,j=0;i<s.size()&&j<t.size();i++){
        if(s[i]<t[j])
        {
            s[i] = t[j];
            j++;
        }
    }
    cout<<s<<endl;

}
