class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        int n=str1.length();
        int m=str2.length();
        if(n < m){
            return gcdOfStrings(str2,str1);
        }
        else if(str1.find(str2)!=0){
            return "";
        }
        else if(str2==""){
            return str1;
        }
        else{
            return gcdOfStrings(str1.substr(m),str2);
        }
        
    }
};