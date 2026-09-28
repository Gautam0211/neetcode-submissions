class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n =nums.size();
        vector<int> res;
        vector<pair<int,int>> v;

        for(int i =0;i<n;i++){
            v.push_back({nums[i],i});
        }
        int l =0,r=n-1;
        sort(v.begin(),v.end());
        while(l<r){
            int sum=v[l].first + v[r].first;

            if(sum==target){
                res.push_back(v[l].second);
                res.push_back(v[r].second);
                break;

            }
            if(sum>target){
                r--;
            }
            else if(sum<target){
                l++;
            }
        }
        sort(res.begin(),res.end());

        return res;
        
    }
};
