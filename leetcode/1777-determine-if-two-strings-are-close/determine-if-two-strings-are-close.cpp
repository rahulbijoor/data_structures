class Solution {
public:
    bool closeStrings(string word1, string word2) {
        array<int,26> fq1={0};
        array<int,26> fq2={0};
        if(word1.length()!=word2.length()){
            return false;
        }
        for(int i=0;i<word1.length();i++){
            int ind=word1[i]-'a';
            fq1[ind]++;
        }
        for(int j=0;j<word2.length();j++){
            int ind=word2[j]-'a';
            fq2[ind]++;
        }
        for(int i=0;i<26;i++){
            if((fq1[i]==0 && fq2[i]!=0)||(fq1[i]!=0 && fq2[i]==0)){
                return false;
            }
        }
        sort(fq1.begin(),fq1.end());
        sort(fq2.begin(),fq2.end());
        for(int i=0;i<26;i++){
            if(fq1[i]!=fq2[i]){
                return false;
            }
        }
        return true;
    }
};