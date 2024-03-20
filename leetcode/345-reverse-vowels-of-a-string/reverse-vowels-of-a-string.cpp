class Solution {
public:
    string reverseVowels(string s) {
        vector<char> vowels;
        for(int i=0;i<s.length();i++){
            if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U'){
                vowels.push_back(s[i]);
            }
        }
        int ind=vowels.size()-1;
        string result="";
        for(int i=0;i<s.length();i++){
             if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U'){
                result+=vowels[ind--];
             }
             else{
                result+=s[i];
             }
        }
        return result;
    }
};