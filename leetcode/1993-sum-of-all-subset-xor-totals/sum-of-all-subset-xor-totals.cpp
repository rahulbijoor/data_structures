class Solution {
public:
    int recXORSum(vector<int>& nums, int index, int sum){
        if(index == nums.size()){
            return sum;
        }
        int taken = recXORSum( nums, index+1, sum^nums[index]);
        int nottaken = recXORSum( nums, index+1, sum);
        return taken+nottaken; 
    }
    int subsetXORSum(vector<int>& nums) {
        return recXORSum(nums,0,0);

    }
};