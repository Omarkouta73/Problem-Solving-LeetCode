// https://codeforces.com/gym/104426/problem/H
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    
    int t = 0, f= 0, m = 0, i = 0;
    cin >> t;
    
    while (t > 0){
        unordered_map<int, int> ca, cb;
        cin >> f >> m;
    
        vector<int> a(f), b(f);
    
        for (i = 0; i < f; i++)
            cin >> a[i];
        
        for (i = 0; i < f; i++)
            cin >> b[i];
    
        
        for (int x : a) ca[x]++;
        for (int x : b) cb[x]++;
        
        int happy = 0;
        for (auto& p : ca){
            happy += min(ca[p.first], cb[p.first]);
        }
        
        cout << happy << '\n';
        
        
        t--;
    }

    return 0;
}