class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        hash_map={}
        for ch in range(0,len(s1)):
            hash_map[s1[ch]]=hash_map.get(s1[ch],0)+1
        l=0
        r=len(s1)-1
        freq_map={}
        # while r<len(s2) and l<=r:
        for ch in range(l,r+1):
            freq_map[s2[ch]]=freq_map.get(s2[ch],0)+1
        if freq_map==hash_map:
            return True
        else:
            freq_map[s2[l]]-=1
            if freq_map[s2[l]]==0:
                del freq_map[s2[l]]
                         
            l+=1
            if r==len(s2)-1:
                return False
            r+=1
            freq_map[s2[r]]=freq_map.get(s2[r],0)+1
        while r<len(s2) and l<=r:
            if freq_map==hash_map:
                return True
            else:
                freq_map[s2[l]]-=1
                if freq_map[s2[l]]==0:
                    del freq_map[s2[l]]
                l+=1

                if r==len(s2)-1:
                    break        
                r+=1
                freq_map[s2[r]]=freq_map.get(s2[r],0)+1     
        return False

            



        
