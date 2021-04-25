#include <iostream>
#include <stack>
#include <vector>
#include <map>
#include <array>
#include <list>
#include <set>
#include <deque>
#include <iterator>
#include <queue>
#include <algorithm>
#include <numeric>
#include <ostream>
#include <iomanip>
#include <cstdlib>
#include <sstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <valarray>

using namespace std;
#define vectorofint  vector<int>
#define vectorofstring vector<string>
#define vectoroflong vector<long>
#define vectoroflonglong vector<long long>
#define input(x) cin>>x
#define print(x) cout<<x<<" "
#define println(x) cout<<x<<endl
#define newline() cout<<endl;
#define loop(i,n) for(int i=0; i<n; i++)
template<typename first,typename second, typename input>
map<first,second> counter( input & obj ){
    map<first,second>ans;
    for(first i : obj){
        ans[i]++;
    }
    return ans;
}
void inputvector(vector <int>& v,int n){
    loop(i,n){
        int next;input(next);
        v[i]=next;
    }
}
int stringtoint(string & s){
    stringstream mystream(s);
    int ans;
    mystream>>ans;
    return ans;
}
void solve(vectorofint &v,int target){

}
int main() {
    int n;
    input(n);
    vector<int>v1(n);
    vector<int>v2(n-1);
    vector<int>v3(n-2);
    inputvector(v1,n);
    inputvector(v2,n-1);
    inputvector(v3,n-2);
    int sum1=0,sum2=0,sum3=0;
    sum1= accumulate(v1.begin(),v1.end(),0);
    sum2= accumulate(v2.begin(),v2.end(),0);
    sum3= accumulate(v3.begin(),v3.end(),0);
    println(sum1-sum2);
    println(sum2-sum3);
//    loop(i,n) {
//        int value;input(value);
//        v[i]=value;
//    }

}
