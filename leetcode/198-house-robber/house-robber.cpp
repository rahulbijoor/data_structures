class Solution {
public:
    int __rob(vector<int> &nums,int index,vector<int> &memo){
        if(index == 0){
            return nums[0];
        }
        if(index < 0){
            return 0;
        }
        if(memo[index] != -1){
            return memo[index];

        }
        int pick = nums[index] + __rob(nums,index-2,memo);
        int notpick = __rob(nums,index-1,memo);
        memo[index] = max(pick,notpick);
        return memo[index];
    }
    int rob(vector<int>& nums) {
        int len=nums.size();
        vector<int> memo(len+1,-1);
        return __rob(nums,len-1,memo);
    }
};