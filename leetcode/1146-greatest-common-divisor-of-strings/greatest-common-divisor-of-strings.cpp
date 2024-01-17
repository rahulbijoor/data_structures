class Solution {
public:
    int gcd(int a,int b){
        if(a==0){
            return b;
        }
        if(b==0){
            return a;
        }
        if(a>b){
            return gcd(a-b,b);
        }
        return gcd(b-a,a);
    }
    string gcdOfStrings(string str1, string str2) {
        if(str1+str2==str2+str1){
            return str1.substr(0,gcd(str1.length(),str2.length()));
        }
        return "";
    }
};