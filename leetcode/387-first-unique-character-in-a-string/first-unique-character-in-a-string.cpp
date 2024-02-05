class Solution {
public:
    int firstUniqChar(string s) {
        int arr[26]={0};
        for(int i=0;i<s.length();i++){
            int ch=s[i]-'a';
            arr[ch]++;
        }
        for(int i=0;i<s.length();i++){
             int ch=s[i]-'a';
             if(arr[ch]==1){
                 return i;
             }
        }
        return -1;
    }
};