class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
      vector<int> from(n+1);
      vector<int> to(n+1);
      for(int i=0;i<trust.size();i++){
          from[trust[i][0]]++;
          to[trust[i][1]]++;
        
      }
      for(int i=1;i<=n;i++){
          if(from[i]==0 && to[i]==n-1){
              return i;
          }
          
      }
      return -1;
    }
};