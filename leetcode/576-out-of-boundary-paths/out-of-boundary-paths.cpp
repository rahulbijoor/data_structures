class Solution {
public:
    const int mod=1e9+7;
   /* int __findPaths(int m,int n,int maxMove,int i,int j,int moves){
        if(moves>maxMove){
            return 0;
        }
        if(i<0||j<0||i>m-1||j>n-1){
            return 1;
        }
        int top=__findPaths(m,n,maxMove,i-1,j,moves++);
        int down=__findPaths(m,n,maxMove,i+1,j,moves++);
        int left=__findPaths(m,n,maxMove,i,j-1,moves++);
        int right=__findPaths(m,n,maxMove,i,j+1,moves++);
        return top+down+left+right;
    }*/
     int recursion(int m , int n , int maxMove, int startRow, int startColumn,vector<vector<vector<int>>> &memo){

        if(maxMove < 0){
            return 0;
        }
        
        if(startRow  > m-1 || startRow < 0 || startColumn > n-1 || startColumn < 0){
            return 1;
        }
        if(memo[startRow][startColumn][maxMove]!=-1){
            return memo[startRow][startColumn][maxMove]%mod;
        }
        
        int up = recursion(m,n,maxMove-1,startRow -1,startColumn,memo)%mod;
        int down = recursion(m,n,maxMove-1,startRow + 1,startColumn,memo)%mod;
        int left = recursion(m,n,maxMove-1,startRow,startColumn -1,memo)%mod;
        int right = recursion(m,n,maxMove-1,startRow,startColumn+1,memo)%mod;
        memo[startRow][startColumn][maxMove] = ((up + down)%mod + (left + right)%mod)%mod;
        return memo[startRow][startColumn][maxMove];
    }
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        vector<vector<vector<int>>> memo(m, vector<vector<int> >(n, vector<int>(maxMove+1,-1)));
        return recursion(m,n,maxMove,startRow,startColumn,memo);
    }
};