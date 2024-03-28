class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int ans=0,left=0;
        unordered_map<int,int> umap;
        for(int i=0;i<nums.size();i++){
            umap[nums[i]]+=1;
            while(umap[nums[i]]>k){
                umap[nums[left]]-=1;
                left+=1;
            }
            ans=max(ans,(i-left) +1);
        }
        return ans;
    }
};