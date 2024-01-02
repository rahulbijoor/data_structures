class Solution {
public:
    int __maxSatisfaction(vector<int>& satisfaction,int index,int count,vector<vector<int>>& memo){
        if(index==satisfaction.size()){
            return 0; 
        }
        if (memo[index][count]!=-1){
            return memo[index][count];
        }
        int choose=satisfaction[index]*(count)+__maxSatisfaction(satisfaction,index+1,count+1,memo);
        int notchoose=__maxSatisfaction(satisfaction,index+1,count,memo);
        memo[index][count]=max(choose,notchoose);
        return memo[index][count];
    }
    int maxSatisfaction(vector<int>& satisfaction) {
        int count=1;
        sort(satisfaction.begin(),satisfaction.end());
        int n=satisfaction.size();
        vector<vector<int>> memo(n+1,vector<int>(n+1,-1));
        return __maxSatisfaction(satisfaction,0,count,memo);
        
    }
};