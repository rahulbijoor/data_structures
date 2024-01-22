class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        vector<int> result;
        int sum=0;
        int asum=0;
        int n=nums.size();
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]==nums[i+1]){
                result.push_back(nums[i]);
            }
            sum+=nums[i];
        }
        sum+=nums[n-1];
        asum=(n*(n+1))/2;
        sum-=result[0];
        result.push_back(asum-sum);
        return result;
    }
};