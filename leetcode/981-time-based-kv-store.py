class TimeMap:
    def __init__(self):
        self.keystore = {}    

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.keystore.get(key, [])
        res =  ""
        l, r = 0, len(values)-1
        while l <= r:
            m = l + (r-l)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else: 
                r = m - 1
        return res


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
param_2 = obj.get("foo",2)
print(param_2)
