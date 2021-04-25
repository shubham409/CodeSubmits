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
    vector<int>vl(n);
    loop(i,n) {
        int value;input(value);
        vl[i]=value;
    }
    sort(vl.begin(),vl.end());
    int q;
    input(q);
    loop(i,q){
        int search;
        input(search);
        search=upper_bound(vl.begin(),vl.end(),search)-vl.begin();
        println(search);
    }

}
