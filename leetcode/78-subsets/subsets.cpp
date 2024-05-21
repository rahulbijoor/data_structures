class Solution {
public:
    void recSubsets(vector<int>& nums, int index,vector<int>& subset,vector<vector<int>>& powersets){
        powersets.push_back(subset);
        for(int i=index;i<nums.size();i++){
            subset.push_back(nums[i]);
            recSubsets(nums,i+1,subset,powersets);
            subset.pop_back();
        }


    }
    
    vector<vector<int>> subsets(vector<int>& nums) {
      vector<vector<int>> powersets;
      vector<int> subset;
      recSubsets(nums,0,subset,powersets); 
      return powersets;
    }
};