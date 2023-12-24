class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        int max=0;
        for(int i=0;i<points.size();i++){
            cout<<"["<<points[i][0]<<" , "<<points[i][1]<<"]"<<" , ";
        }
        cout<<endl;
        sort(points.begin(),points.end());
        for(int i=0;i<points.size();i++){
            cout<<"["<<points[i][0]<<" , "<<points[i][1]<<"]"<<" , ";
        }
        for(int i=0;i<points.size()-1;i++){
            if(max<points[i+1][0]-points[i][0]){
                max=points[i+1][0]-points[i][0];
            }
        }
        return max;
    }
};