class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        hash_map={}
        l=0
        r=0
        while r<len(s):
                if s[r] in hash_map:
                    l=max(l,hash_map[s[r]]+1)                    

                maxi=max(maxi,r-l+1)
                hash_map[s[r]]=r   
                r+=1 
        return maxi        
