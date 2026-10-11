class TimeMap:

    def __init__(self):
        self.data={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key]=[]

        self.data[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        array=self.data[key]
        l=0
        h=len(array)-1

        while l<=h:
            m=(l+h)//2
            if array[m][0]==timestamp:
                return array[m][1]
            elif array[m][0]<=timestamp:
                l=m+1
            else:
                h=m-1 
        if h<0:
            return ""        
        return array[h][1]              

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)