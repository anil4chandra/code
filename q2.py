#include <iostream>

using namespace std;

int main()
{
    string a;
    cin>>a;
    int u,n=0;
    for(u=0;a[u]!='\0';u++)
    {
        n++;
    }
    string b;
    cin>>b;
    int i,l=0;
    for(i=0;b[i]!='\0';i++)
    {
        l++;
    }
    char last;
    last=b[l-1];
    int result=0;
    int y;
    for(y=0;y<n;y++)
    {
        if(a[y] == last)
        {
            result++;
        }
    }
    cout<<result;

    return 0;
}
