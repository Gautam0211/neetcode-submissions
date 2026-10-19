class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l=0
        r=0
        update=False
        sum=nums[l]
        mini=len(nums)
        while r<len(nums) and l<=r:
            # if l==r:
                # sum=nums[l]
            if sum<target:
                r+=1
                if r<len(nums):
                    sum+=nums[r]
            else:
                mini=min(mini,r-l+1)
                update=True
                sum-=nums[l]
                l+=1
        if update==False:
            return 0    
        return mini        



        


        