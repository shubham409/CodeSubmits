#include <iostream>
#include<set>
#include <map>
#include <vector>
#include <numeric>
#include <string>
#include <algorithm>
#include <iterator>
#include <math.h>
using namespace std;
#define print(x) cout << x<<endl
#define input(x) cin >> x
#define ll long long  

int main() {
    // ios_base::sync_with_stdio(0);
    // cin.tie(0);
    // cout.tie(0);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);    
    // map <char, int>m;
    // string s;
    // cin>>s;
    // string ::iterator it;
    // it=s.begin();
    
    // while (it != s.end())
    // {
    //     // char c =*it;
    //     // // if
    //     // cout<<c<<endl;
    //     // it=next(it);
    // }
    int n;
    input(n);
    if (n==0 || n==1) 
    {   
        print(0);
        return 0;
    }

    if(n%2==0){
       ll ans = pow(2,n/2);
       print(ans);

    }
    else{
        print(0);
    }
    
}