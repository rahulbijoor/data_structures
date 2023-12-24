class Solution {
public:
    int minOperations(string s) {
        int c1=0; //count for string starting with 0
        int c2=0; // string for staring with 1
        for(int i=0;i<s.length();i++)
        {
            if(i%2==0){
                if(s[i]=='0'){
                    c2++;
                }
                else{
                    c1++;
                }
            }
            else if(i%2!=0){
                if(s[i]=='0'){
                    c1++;
                }
                else{
                    c2++;
                }
            }
        }
        return min(c1,c2);
    }
};