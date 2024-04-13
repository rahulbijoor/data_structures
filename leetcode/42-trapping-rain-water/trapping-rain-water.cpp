class Solution {
public:
    int trap(vector<int>& height) {
        //find the water stored in each index
        // water stored per position i= min(leftMAX(i),rightMAX(i))-height[i]
        int l=height.size();
        int left=0;
        int right=l-1;
        int lmax=0;
        int rmax=0;
        int water=0;
        while(left<=right){
            if(height[left]<=height[right]){
                if(height[left] >= lmax ){
                    lmax=height[left];
                }
                else{
                    water+=lmax-height[left];
                }
                left++;
            }
            else{
                if(height[right] >=rmax){
                    rmax=height[right];
                }
                else{
                    water+=rmax-height[right];
                }
                right--;
            }
        }
        return water;
    }
};