#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int solve(int i,int buying,vector<int>&prices,map<pair<int,int>,int>& memo){
        if (i >= prices.size()) return 0;
        
        if (memo.find({i, buying}) != memo.end()){
            return memo[{i, buying}];
        }
        
        if (buying){
            int buy = this->solve(i+1, !buying, prices, memo) - prices[i];
            int cooldown = this->solve(i+1, buying, prices, memo);
            memo[{i, buying}] = max(buy, cooldown);
        }
        else {
            int sell = this->solve(i+2, !buying, prices, memo) + prices[i];
            int cooldown = this->solve(i+1, buying, prices, memo);
            memo[{i, buying}] = max(sell, cooldown);
        }
        
        return memo[{i, buying}];
    }
    int maxProfit(vector<int>& prices) {
         map<pair<int, int>, int> memo;
        return this->solve(0, 1, prices, memo);
    }
};