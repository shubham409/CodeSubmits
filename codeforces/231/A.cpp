#include <iostream>
#include <algorithm>
#include <functional>
#include <cassert>
#include <iterator>
#include <array>
#include <vector>
using namespace std;

int main(int argc, char const *argv[])
{
    int a;
    cin>>a;
    vector <int>v;
    int val=0;
    for (int i = 0; i < a; i++)
    {
        int temp=0 ;
        for (int i = 0; i < 3; i++)
        {
            int num=0;
            cin>>num;
            temp+=num;
        }
        if(temp>=2)
        {
            val++;
        }
    }
    cout<<(val);
    return 0;
}