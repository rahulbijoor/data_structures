class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int count=0,zerocount=0,onecount=0;
        unordered_map<int,int> umap;
        umap[0]=-1;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                zerocount++;
            }
            else{
                onecount++;
            }
            int diff=zerocount-onecount;
            if(umap.find(diff) == umap.end()){
                umap[diff]=i;
            }
            else{
                count=max(count,i-umap[diff]);
            }
        }
        cout<<(2*min(zerocount,onecount));
        return count;
    }
};