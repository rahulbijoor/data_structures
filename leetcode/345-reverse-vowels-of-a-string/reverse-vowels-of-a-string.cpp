class Solution {
public:
    string reverseVowels(string s) {
        string ch="";
        for( int i = s.length() - 1 ; i >= 0 ; i-- ){
            if( s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U'){
                ch+=s[i];
            }
        }
        int ind=0;
        string result="";
        for( int j = 0; j < s.length(); j++ ){
            if(s[j] == 'a' || s[j] == 'e' || s[j] == 'i' || s[j] == 'o' || s[j] == 'u' || s[j] == 'A' || s[j] == 'E' || s[j] == 'I' || s[j] == 'O' || s[j] == 'U'){
                result+=ch[ind++];
            }
            else{
                result+=s[j];
            }
        }
        return result;
    }
};