class Solution {
public:
    string minRemoveToMakeValid(string s) {
        int open=0;
        int close=0;
        stack<char> st;
        for(int i=0;i<s.length();i++){
            char currentChar=s[i];
            if(currentChar=='('){
                open++;
            }
            if(currentChar==')'){
                close++;
            }
            if(close>open){
                close--;
                continue;
            }
            else{
                st.push(currentChar);
            }
        }
        string result="";
        while (!st.empty()) {
            char currentChar = st.top();
            st.pop();
            if(open>close && currentChar =='('){
                open--;
            }
            else{
                result+=currentChar;
            }
        }
        reverse(result.begin(),result.end());
        return result;

    }
};