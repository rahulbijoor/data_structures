class Solution {
public:
    int climbStairs(int n,vector<int> &memo) {
        if(n<=2){
            return n;
        }
        if(memo[n]!=-1){
            return memo[n];
        }
        memo[n]=climbStairs(n-1,memo)+climbStairs(n-2,memo);
        return memo[n];
    }
    int climbStairs(int n){
        int dp[n+1];
        if(n<=2){
            return n;
        }
        dp[0]=0;
        dp[1]=1;
        dp[2]=2;

        for(int i=3;i<n+1;i++){
            dp[i]=dp[i-1]+dp[i-2];
        }
        return dp[n];
    }
};