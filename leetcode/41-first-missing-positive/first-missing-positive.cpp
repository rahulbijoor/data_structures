class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int length=nums.size();
        int i=0;
        while(i<length && nums[i]<=0){
            i++;
        }
        if(i==length){
            return 1;
        }
        int c=1;
        while(i<length){
            if(nums[i]!=c)
                return c;
            while(i<length && nums[i]==c){
                i++;
            }
            c++;
        }
        return c;
    }
};