class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        maxi=0
        hash_map={}
        while r<len(s):
            hash_map[s[r]]=hash_map.get(s[r],0)+1
            max_freq=max(hash_map.values())
            req=abs(r-l+1-max_freq)
            if req>k:
                hash_map[s[l]]-=1
                l+=1
                max_freq=max(hash_map.values())
                req=abs(r-l+1-max_freq)
            maxi=max(maxi,max_freq+req)
            r+=1    
        return maxi    