class Solution {
public:
    int minPartitions(string n) {
        int max=0;
        for(int i=0;i<n.length();i++){
            int digit=(int)n[i]-48;
        
            if(digit>max){
                max=digit;
            }
        }
        return max;
    }
};