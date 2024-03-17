class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;
        int start=newInterval[0],end=newInterval[1];
        bool inserted=false;
        for(int i=0;i<intervals.size();i++){
            int cstart=intervals[i][0],cend=intervals[i][1];
            if(cend<start || inserted){
                result.push_back({cstart,cend});
                continue;
            }
            start=min(start,cstart);
            if(end<cstart){
                result.push_back({start,end});
                result.push_back({cstart,cend});
                inserted=true;
                continue;
            }
            if(end<=cend){
                result.push_back({start,cend});
                inserted=true;
            }
            }
            if(!inserted){
                result.push_back({start,end});
            }
            
            return result;
        }
    
};