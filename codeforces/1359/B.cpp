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
/*
    Author : Shubham Kumar Mishra
    ID : shubham_409
*/
// My Macros
#define vectorofint vector<int>
#define vectorofstring vector<string>
#define vectoroflong vector<long>
#define vectoroflonglong vector<long long>
#define input(x) cin >> x
#define print(x) cout << x << " "
#define println(x) cout << x << endl
#define newline() cout << endl;
#define loop(i, n) for (int i = 0; i < n; i++)
#define loopfrom(i, j, n) for (int i = j; i < n; i++)
#define get(i) int i; input(i)
#define gets(i, j) int i, j; input(i); input(j)
#define getall(i, j, k) int i, j, k; input(i); input(j);  input(k)
#define getfour(i, j, k, l) int i, j, k, l; input(i); input(j);  input(k);  input(l)
#define getstr(s)  string s; input(s)

// My Functions
template <typename first, typename second, typename input>
map<first, second> counter(input &obj)
{
    map<first, second> ans;
    for (first i : obj)
    {
        ans[i]++;
    }
    return ans;
}
template<typename type>
void getvector(vector<type> &v, type n)
{
    loop(i, n)
    {
        type next;
        input(next);
        v[i] = next;
    }
}
void getvector(vector<int> &v, int n)
{
    loop(i, n)
    {
        int next;
        input(next);
        v[i] = next;
    }
}
void inputvector(vector<int> &v, int n)
{
    loop(i, n)
    {
        int next;
        input(next);
        v[i] = next;
    }
}
void prefixsum(vector<int> &v, int n)
{
    loopfrom(i, 1, n)
    {
        v[i] = v[i - 1] + v[i];
    }
}
int stringtoint(string &s)
{
    stringstream mystream(s);
    int ans;
    mystream >> ans;
    return ans;
}
void solve(vectorofint &v, int target)
{
}
void input_predicate(int &i)
{
    input(i);
}
void output_predicate(int &i)
{
    println(i);
}
void increment_predicate(int &i)
{
    i = i + 1;
}

// My Code
void solve()
{
    getfour(n,m,x,y);
    int ans=0;
    loop(i,n){
        getstr(s);
        int one=0,two=0;
        
        one += count(s.begin(), s.end(), '.');
        int pos =s.find("..",0);
        while (pos != string:: npos)
        {
            two++;
            pos = s.find("..", pos + 2);
        }
        if(2*x<=y){
            ans += (one ) * x;
        }
        else{
            ans+=(two*(y));
            ans += (one - two*2) * x;
        }
    }       
    println(ans);
}
int main()
{
    get(t);
    loop(i, t)
    {
        solve();
    }
}