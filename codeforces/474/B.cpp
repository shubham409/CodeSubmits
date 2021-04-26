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
#define loopfrom(i,j,n) for(int i=j; i<n; i++)
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
void prefixsum(vector <int>& v,int n){
    loopfrom(i,1,n){
        v[i]=v[i-1]+v[i];
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
    vector<int>v(n);
    inputvector(v,n);
    prefixsum(v,n);
    int q;
    input(q);
    loop(i,q){
        int search;
        input(search);
        search=lower_bound(v.begin(),v.end(),search)-v.begin();
        println(search+1);
    }
    
    


}
