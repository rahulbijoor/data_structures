class Solution {
public:
   int numDecodings(int index,string s,vector<int> &memo){
        if(index==s.length()){
            return 1;
        }
        if(s[index]=='0'){
            return 0;
        }
        if(memo[index]!=-1){
            return memo[index];
        }
        memo[index]=numDecodings(index+1,s,memo);
        if(index+1<s.length() && (s[index]=='1' || (s[index]=='2' && s[index+1]<='6'))){
            memo[index]+=numDecodings(index+2,s,memo);
        }
        return memo[index];
    }
    int numDecodings(string s) {
        vector<int> memo(s.length(),-1);
        return numDecodings(0,s,memo);
    }
};