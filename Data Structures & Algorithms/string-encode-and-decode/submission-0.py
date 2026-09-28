class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=""
        for word in strs:
            enc+=str(len(word))+"&"+ word
        return enc    

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            j=i
            while s[j] != '&':
                j+=1
            lenght=int(s[i:j])
            j+=1
            word=s[j:j+lenght]
            ans.append(word)

            i=j+lenght
        return ans           
