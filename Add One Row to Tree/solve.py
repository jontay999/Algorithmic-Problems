from collections import OrderedDict
from bisect import bisect_right, insort
class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = {}
            self.d[key]["arr"] = []
            self.d[key]["dic"] = {}
        self.d[key]["arr"].append(timestamp)
        self.d[key]["dic"][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return ""
        arr = self.d[key]["arr"]
        idx = bisect_right(arr, timestamp)
        if idx == 0:
            return ""
        return self.d[key]["dic"][arr[idx-1]]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)