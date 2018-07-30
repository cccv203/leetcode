#include <iostream>
#include<string>

using namespace std;

int main()
{
    string str;
    cin>>str;
    float nums=0,cls=0,temp=1;

    for(int j=0;j<str.size()-1;j++){
        if(str[j+1]==str[j]){
            temp+=1;

        }
        else{
            nums += temp;
            cls++;
            temp=1;
        }
    }
    printf("%.2f",((nums+temp)/(cls+1)));
}
