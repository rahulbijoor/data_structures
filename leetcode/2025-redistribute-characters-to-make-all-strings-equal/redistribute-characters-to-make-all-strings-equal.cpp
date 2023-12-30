class Solution {
public:
    bool makeEqual(vector<string>& words) {
        int freq[26]={0};
        for(int i=0;i<words.size();i++){
            for(int j=0;j<words[i].length();j++){
                int ind=words[i][j]-'a';
                freq[ind]++;
            }
        }
        for(int i=0;i<26;i++){
            if(freq[i]!=0 && freq[i]%words.size()!=0){
                    return false;
            }
        }
        return true;
    }
};