class Solution {
public:
    const int mod=1e9+7;
    int kInversePairs(int n, int k) {
        vector<vector<int>> dp(n+1,vector<int>(k+1,0));
        for(int i=1;i<n+1;i++){
            dp[i][0]=1;
        }
        for(int i=2; i < n+1; i++){
            for(int j=1; j < k+1; j++){
                dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod;
                if( j >= i)
                    dp[i][j]=(dp[i][j]-dp[i-1][j-i]+mod)%mod;
            }
        }
        return dp[n][k];
    }
};