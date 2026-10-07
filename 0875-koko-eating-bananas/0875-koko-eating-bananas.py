class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l=1
        hh=max(piles)
        m=(l+hh)//2
        while l<=hh:
            m=(l+hh)//2
            sum=0
            for i in piles:
                sum= sum+ math.ceil(i/m)
            if sum<= h:
                hh=m-1 
            else:
                l=m+1
        return l             



        