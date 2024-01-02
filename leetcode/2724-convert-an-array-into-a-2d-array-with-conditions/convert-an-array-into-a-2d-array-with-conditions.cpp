class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        unordered_map<int,int>umap;
        int num=0;
        for(int i=0;i<nums.size();i++){
            if(umap.find(nums[i])!=umap.end()){
                umap[nums[i]]++;
            }
            else{
                umap[nums[i]]=1;
            }
            num=max(umap[nums[i]],num);
        }
        vector<vector<int>> result;
        for(int i=0;i<num;i++){
            vector<int> row;
            for(auto item = umap.begin(); item != umap.end();){
                if(item->second!=0){
                    cout<<item->first<<" : "<<item->second<<endl;
                    row.push_back(item->first);
                    item->second--;
                    item++;
                }
                else{
                    item=umap.erase(item);
                }
               

            }
            result.push_back(row);
        }
        return result;
    }
};