class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hash_map={}
        for i in range(len(numbers)):
            hash_map[numbers[i]]=i    
        for i in range(len(numbers)):
            complement=target-numbers[i]
            if complement in hash_map:
                return[i+1,hash_map[complement]+1]    
                break

        
        