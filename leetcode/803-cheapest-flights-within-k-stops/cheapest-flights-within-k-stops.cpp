class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<pair<int,int>> adj[n];
        for(auto flight : flights){
            adj[flight[0]].push_back({flight[1],flight[2]});
        }
        queue<pair<int, pair<int, int>>> q;
        q.push({0,{src,0}});
        vector<int> dist(n,1e9);
        dist[src]=0;
        while(!q.empty()){
            auto i=q.front();
            int stops=i.first;
            int node=i.second.first;
            int cost=i.second.second;
            q.pop();
            if(stops>k){
                continue;
            }
            for(auto x : adj[node]){
                int adjNode = x.first;
                int edW=x.second;
                if(cost+edW < dist[adjNode] && stops <=k){
                    dist[adjNode]=cost+edW;
                    q.push({stops+1,{adjNode,dist[adjNode]}});
                }
            }
            
        }
            if(dist[dst]==1e9) return -1;
            return dist[dst]; 
    }
};