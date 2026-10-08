class Solution:
    def findMin(self, nums: list[int]) -> int:
        l=0
        h=len(nums)-1
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            mid=(l+h)//2
            if nums[mid]<nums[h]:
                h=mid
            elif nums[mid]>nums[h]:
                l=mid+1    
            # if nums[mid-1]<nums[mid] and nums[mid]<nums[mid+1]:
                # h=mid-1
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return nums[mid+1]
            elif nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]:
                return nums[mid]        

                
        