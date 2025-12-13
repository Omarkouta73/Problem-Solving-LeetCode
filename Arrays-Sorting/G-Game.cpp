// https://codeforces.com/gym/104426/problem/A
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t = 0, n = 0, P = 0, Q = 0;
    cin >> t;
    
    while (t > 0){
        cin >> n >> P >> Q;
        vector<long long> pos, neg;
        for (int i = 0; i < n; i++){
            long long x;
            cin >> x;
            if (x > 0){
                pos.push_back(x);
            }
            else if (x < 0) {
                neg.push_back(x);
            }
        }
        sort(pos.begin(), pos.end(), greater<int>());
        sort(neg.begin(), neg.end());
        
        long long sa=0, sb=0;
        for (int i = 0; i < min(P, (int)pos.size()); i++){
            sa+=pos[i];
        }
        for (int i = 0; i < min(Q, (int)neg.size()); i++){
            sb+=neg[i];
        }
        
        cout << sa - sb << '\n';
        
        t--;
    }

    return 0;
}