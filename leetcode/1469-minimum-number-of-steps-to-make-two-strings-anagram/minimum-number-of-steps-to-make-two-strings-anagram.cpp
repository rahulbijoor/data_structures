class Solution {
public:
    int minSteps(string s, string t) {
        int fq[26]={0};
        for(int i=0;i<s.length();i++){
            int ind=s[i]-'a';
            fq[ind]++;
        }
        for(int i=0;i<t.length();i++){
            int ind=t[i]-'a';
            fq[ind]--;
        }int sum=0;
        for(int i=0;i<26;i++){
            sum+=abs(fq[i]);
        }
        return sum/2;
    }
};