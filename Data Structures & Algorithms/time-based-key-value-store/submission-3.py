class TimeMap:

    def __init__(self):
        self.store = {} # key str : value { key int, value str }
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if the key exists add to the keys value dict
        if key in self.store:
            self.store[key][timestamp] = value
        else: 
            self.store[key] = {}
            self.store[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            if timestamp in self.store[key]:
                return self.store[key][timestamp]
            maxseen = 0
            for i in self.store[key]:
                if i <= timestamp:
                    maxseen = max(maxseen, i)
            if maxseen == 0:
                return ""
            return self.store[key][maxseen]
        return ""
