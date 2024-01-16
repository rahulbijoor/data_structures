class RandomizedSet {
public:
    vector<int> randomset;
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if(find(randomset.begin(),randomset.end(),val)==randomset.end()){
            randomset.push_back(val);
            return true;
        }
        return false;

    }
    
    bool remove(int val) {
        
         auto it = std::find(randomset.begin(), randomset.end(), val);


    if (it != randomset.end()) {
        randomset.erase(it); 
        return true;
    }
    return false;
    }
    
    int getRandom() {
        int l=randomset.size();
        int ind=rand()%l;
        return randomset[ind];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */