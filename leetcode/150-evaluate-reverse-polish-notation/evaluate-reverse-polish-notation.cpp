class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for(int i=0;i<tokens.size();i++){
            if(tokens[i]=="+"||tokens[i]=="-"||tokens[i]=="*"||tokens[i]=="/"){
                int opt2=st.top();
                st.pop();
                int opt1=st.top();
                st.pop();
                if(tokens[i]=="+"){
                    st.push(opt1+opt2);
                }
                else if(tokens[i]=="-"){
                     st.push(opt1-opt2);
                }
                else if(tokens[i]=="*"){
                     st.push(opt1*opt2);
                }
                else if(tokens[i]=="/"){
                     st.push(opt1/opt2);
                }
            }
            else{
                int opt=stoi(tokens[i]);
                st.push(opt);
            }
        }
        return st.top();
    }
};