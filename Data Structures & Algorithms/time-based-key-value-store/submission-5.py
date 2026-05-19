class TimeMap:

    def __init__(self):
        self.store = {} # key str : value { key int, value str }
        self.store_list = {} # here for each new timestore we just append 

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if the key exists add to the keys value dict
        # We know the timestamp values are added sequentially so use a list
        # since they are sequential the values would be sorted
        if key in self.store:
            self.store[key][timestamp] = value
            self.store_list[key].append(timestamp)
        else: 
            self.store[key] = {}
            self.store[key][timestamp] = value
            self.store_list[key] = []
            self.store_list[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            if timestamp in self.store[key]:
                return self.store[key][timestamp]
            # Now we want to perform a binary search if we didn't find the value. 
            # We also know that r points to the largest value smaller than the searched value.
            # We also know that l points to the smallest value larger than the searched value. 
            l, r = 0, len(self.store[key]) -1
            while l<=r:
                m = (l+r)//2
                if self.store_list[key][m] > timestamp:
                    r = m -1
                else:
                    l = m +1
            if r <0:
                return ""
            curr = self.store_list[key][r]
            return self.store[key][curr]
        return ""
