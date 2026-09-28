class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mpp;

        for (int num : nums) {
            mpp[num]++;
        }

        vector<pair<int,int>> freqVec(mpp.begin(), mpp.end());

        sort(freqVec.begin(), freqVec.end(), [](pair<int,int> &a, pair<int,int> &b){
            return a.second > b.second;
        });

        vector<int> res;

        for(int i = 0; i < k; i++){
            res.push_back(freqVec[i].first);
        }

        return res;
    }
};
