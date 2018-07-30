#include <string>
#include<iostream>
#include<set>
using namespace std;
int main()
{
    string A,B;
    cin>>A>>B;
    set<string>s;
    int ans = 0;
    for(int i=0;i<A.size()-B.size()+1;i++){
        string sub = A.substr(i,B.size());
        if(s.count(sub))
            continue;
        s.insert(sub);
        for(int k=0;k<B.size();k++){
            if(sub[k]!= B[k])
                if(B[k]!='?')
                    break;
            if(k==B.size()-1){
                ans++;
            }
        }
    }
    cout<<ans;
}
