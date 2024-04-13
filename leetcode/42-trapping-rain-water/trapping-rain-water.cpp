class Solution {
public:
    int trap(vector<int>& height) {
        //find the water stored in each index
        // water stored per position i= min(leftMAX(i),rightMAX(i))-height[i]
        int l=height.size();
        int leftMax[l];
        int rightMax[l];
        int max=0;
        for(int i=0;i<l;i++){
            if(height[i]>max){
                max=height[i];
            }
            leftMax[i]=max;
            cout<<leftMax[i]<<", ";
        }
        cout<<endl;
        max=0;
        for(int i=l-1;i>=0;i--){
            if(height[i]>max){
                max=height[i];
            }
            rightMax[i]=max;
            cout<<rightMax[i]<<", ";
        }

        int water=0;
        for(int i=0;i<l;i++){
            water+=(min(leftMax[i],rightMax[i])-height[i]);
        }
        return water;
    }
};