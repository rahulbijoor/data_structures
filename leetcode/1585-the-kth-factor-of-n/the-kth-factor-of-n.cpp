class Solution {
public:
    int kthFactor(int n, int k) {
        
        int val=1;
        int count=0;
        for(int i=0;i<n;i++){
            if(n%val++==0){
                
                count++;
                if(count==k){
                    return val-1;
                }
            }
            
        }
        return -1;
    }
};