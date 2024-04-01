
class Solution {
public:
    inline void rtrim(std::string &s) {
    s.erase(std::find_if(s.rbegin(), s.rend(), [](unsigned char ch) {
        return !std::isspace(ch);
    }).base(), s.end());
    }
    int lengthOfLastWord(string s) {
        rtrim(s);
        for(int i=s.length()-1;i>=0;i--){
            if(s[i]==' '){
                return (s.length()-(i+1));
            }
        }
        return s.length();
    }
};