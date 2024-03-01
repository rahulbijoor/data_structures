class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int count1=0;
        string result="";
        for(int i=0;i<s.length();i++){
            if(s[i]=='1'){
                count1++;
            }
        }
        int count0=s.length()-count1;
        for(int i=0;i<count1-1;i++){
            result+="1";
        }
        for(int i=1;i<=count0;i++){
            result+="0";
        }
        result+="1";
        return result;
    }
};