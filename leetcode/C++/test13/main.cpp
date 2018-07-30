#include <iostream>
#include <string>
#include<vector>
#include <algorithm>


using namespace std;


bool compare(string s1, string s2){
    return (s1+s2) > (s2+s1);
}

int main()
{
    int n,j=0,k=0;
    string strs[100];
    scanf("%d",&n);
    for(int i=0;i<n;i++)
        cin>>strs[i];
    sort(strs,strs+n,compare);
    for(int i=0;i<n;i++){
        cout<<strs[i];
    }
}
