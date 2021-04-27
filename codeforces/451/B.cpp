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
void input_predicate(int & i){
    input(i);
}
void output_predicate(int &i)
{
    println(i);
}
void increment_predicate(int & i){
    i=i+1;
}
int main() {
    int n=0;
    input(n);
    vector<int>v(n);
    vector<int>st(n);
    inputvector(v,n);
    copy(v.begin(),v.end(),st.begin());
    sort(st.begin(),st.end());
    int a=-1,b=-1;
    for (int i = 0; i < n; i++) {
        int st_val=st[i];
        int v_val=v[i];
        if(a==-1 && v_val!=st_val){
            a=i;
        }
        else{
            if(v_val!=st_val){
                b=i;
            }
        }

    }
//    println(a<<" "<<b);
    reverse(v.begin()+a,v.begin()+b+1);
//    for_each(v.begin(),v.end(),output_predicate);
    bool ans=is_sorted(v.begin(),v.end());
    if(a==-1 && b==-1){
        println("yes");
        println("1 1");
    }
    else{
        if(ans== true){
            println("yes");
            cout<<a+1<<" "<<b+1<<endl;
        }
        else{
            println("no");
        }
    }
}
