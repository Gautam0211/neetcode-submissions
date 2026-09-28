class Solution {
public:
    vector<int> countBits(int n) {

        vector<int> ans;
        int cnt=0;
        ans.push_back(cnt);
        for(int i =1;i<=n;i++){
            int temp =i;
            while(temp){
                temp=temp&(temp-1);
                cnt++;
            }
            ans.push_back(cnt);
            cnt=0;
        }

        return ans;
        
    }
};
