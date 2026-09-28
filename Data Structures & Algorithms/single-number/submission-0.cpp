class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map <int,int> mpp;
        int n =nums.size();
        for(int i =0;i<n;i++){
            mpp[nums[i]]++;
        }
        for(auto a: mpp){
            if(a.second==1){
                return a.first;
            }
        }

    }
};
