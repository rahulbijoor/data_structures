class Solution {
public:
    bool halvesAreAlike(string s) {
        int count=0;
        for(int i=0;i<s.length()/2;i++){
            int ch=tolower(s[i]);
            if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'){
                count++;
            }
        }
        for(int i=s.length()/2;i<s.length();i++){
            int ch=tolower(s[i]);
            if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'){
                count--;
            }
        }
        if(count==0){return true;}
        return false;
    }
};