class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string word3="";
        int l1=word1.length();
        int l2=word2.length();
        int l=0;
        int i=0;
        int j=0;
        while(i < l1 && j < l2){
            if(l%2==0){
            word3+=word1[i++];
            }
            else{
                word3+=word2[j++];
            }
            l++;
        }
        while(i<l1){
            word3+=word1[i++];
        }
        while(j<l2){
            word3+=word2[j++];
        }
        return word3;
    }

};