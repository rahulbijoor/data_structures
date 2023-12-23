class Solution {
public:
    bool isPathCrossing(string path) {
        int x=0;
        int y=0;
        unordered_map<char,pair<int,int>> umap;
        umap['N']={0,1};
        umap['S']={0,-1};
        umap['W']={-1,0};
        umap['E']={1,0};
        unordered_set<string> visited;
        visited.insert("0,0");

        for (char c : path) {
            pair<int, int> curr = umap[c];
            int dx = curr.first;
            int dy = curr.second;
            x += dx;
            y += dy;
            
            string hash = to_string(x) + "," + to_string(y);
            if (visited.find(hash) != visited.end()) {
                return true;
            }
            
            visited.insert(hash);
        }
        
        return false;
    }
};