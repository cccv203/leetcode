#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s1,s2;
    cin>>s1>>s2;
    if(s2.size()>s1.size()) cout<<"No";

    for(int i=0,j=0;i<s1.size();i++){
       if(s1[i]==s2[j])
           j++;
       if(j==s2.size()){
           cout<<"Yes";
           return 0;
       }
    }
    cout<<"No";

}
